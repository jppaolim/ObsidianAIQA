import os
import re
import time
import requests

import pandas as pd

from dotenv import load_dotenv

from langchain.document_loaders import TextLoader, DirectoryLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import CharacterTextSplitter, MarkdownTextSplitter, RecursiveCharacterTextSplitter

#instructor model : https://arxiv.org/pdf/2212.09741.pdf
from langchain.embeddings import HuggingFaceInstructEmbeddings


from langchain.vectorstores import Chroma

from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# ****************  Load Environemnt

load_dotenv()

LLM = os.environ.get("MODEL")
OPENAI_KEY = os.environ.get("OPENAI_KEY")
PERSIST_DIRECTORY = os.environ.get("PERSIST_DIRECTORY")
DOC_DIRECTORY = os.environ.get("DOC_DIRECTORY")
PRINT_SOURCE = False
INSTRUCT_MODEL=os.environ.get("INSTRUCT_MODEL")
### instructor model is trained on 512 token so roughly up to 2K character. So setting at 1500 we should be good.
# then if we pass 4 documents to the chain it should be OK.   
CHUNK_SIZE=int(os.environ.get("CHUNK_SIZE"))
OVERLAP = 32


# ****************  Document Loader

def load_documents():
    docdirectory = "./" + DOC_DIRECTORY + "/"

    loader = DirectoryLoader(
        docdirectory, glob="**/*.md", loader_cls=UnstructuredMarkdownLoader)
    return loader.load()

# ****************  Create or Load embeddings


def embeddings_function():
    embed_instruction = "Represent the Wikipedia document for retrieval: "
    query_instruction = "Represent the Wikipedia question for retrieving supporting documents : "
    Instructembedding = HuggingFaceInstructEmbeddings(
        model_name=INSTRUCT_MODEL, embed_instruction=embed_instruction, query_instruction=query_instruction)

    return Instructembedding


def create_or_load_db():

    dbfileone = "./" + PERSIST_DIRECTORY + "/chroma-collections.parquet"
    dbfiletwo = "./" + PERSIST_DIRECTORY + "/chroma-embeddings.parquet"

    text_splitter = MarkdownTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=OVERLAP)

    documents = load_documents()

    start_time = time.time()
    texts = text_splitter.split_documents(documents)

    elapsed_time = time.time() - start_time

    textspd = pd.Series(map(lambda x:len(x.page_content), texts))
    stats = textspd.describe()
    print(stats)

    print(f"Loaded {len(documents)} documents from {DOC_DIRECTORY}")
    print(f"Split into {len(texts)} chunks of text (max. {CHUNK_SIZE} char each)")
    print(f"it took  {elapsed_time} seconds to process ")

    if not (os.path.exists(dbfileone) and os.path.exists(dbfiletwo)):


        start_time = time.time()
        
        db = Chroma.from_documents(texts, embeddings_function(), 
                    metadatas=[{"source": str(i)} for i in range(len(texts))], persist_directory=PERSIST_DIRECTORY)
        
        elapsed_time = time.time() - start_time
        print(f"it took  {elapsed_time} seconds to create the database with indicated embeddings ")


    else:
        db = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings_function())
    
    return db 


def main():

    db = create_or_load_db()
    db.persist()

    querybase = db.as_retriever(search_kwargs={"k": 1})

    ###  prepare  

    #callbacks = [StreamingStdOutCallbackHandler()]

    system_template = """You act as an helpful research assistant. The user will ask you a question. Use you own knowledge but also incorporate the following pieces of context to help you answer in the most complete and detailed way.  Make sure your answer is fluid, consistent, logicial and detailed.   
    ----------------
    {context}"""
    
    messages = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]

    PROMPT = ChatPromptTemplate.from_messages(messages)

    chain_type_kwargs = {"prompt": PROMPT}
    #chain_type_kwargs = {}
    
    qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=OPENAI_KEY, temperature=0., max_tokens=1024, verbose=True), chain_type="stuff", retriever=querybase, return_source_documents=True, verbose = True, chain_type_kwargs=chain_type_kwargs)
    qa.combine_documents_chain.verbose = True
    
    #qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=OPENAI_KEY, temperature=0., max_tokens=512), chain_type="refine", retriever=querybase, return_source_documents=PRINT_SOURCE)

    # ****************  Retrieve relevant documents

    # Interactive questions and answers
    while True:
        query = input("\nEnter a query: ")
        if query == "exit":
            break
        
        # Get the answer from the chain
        #res = qa(query)
        qa.run(query)    

        if PRINT_SOURCE:
             answer, docs = res['result'], res['source_documents']
        else:
            answer  = res['result']  

        # Print the result
        print("\n\n> Question:")
        print(query)
        print("\n> Answer:")
        print(answer)
        
        if PRINT_SOURCE:
            # Print the relevant sources used for the answer
            for document in docs:
                print("\n> " + document.metadata["source"] + ":")
                print(document.page_content)

    db = None


if __name__ == "__main__":
    main()