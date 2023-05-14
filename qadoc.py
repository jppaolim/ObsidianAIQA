import os
import re
import time
import requests

from dotenv import load_dotenv

from langchain.document_loaders import TextLoader, DirectoryLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import CharacterTextSplitter, MarkdownTextSplitter, RecursiveCharacterTextSplitter

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



# ****************  Document Loader

def load_documents():
    loader = DirectoryLoader(
        DOC_DIRECTORY, glob="**/*.md", loader_cls=UnstructuredMarkdownLoader)
    return loader.load()

# ****************  Create or Load embeddings


def embeddings_function():
    embed_instruction = "Represent the sentence for retrieval: "
    query_instruction = "Represent the question for retrieving supporting documents to answer it : "
    Instructembedding = HuggingFaceInstructEmbeddings(
        model_name=INSTRUCT_MODEL, embed_instruction=embed_instruction, query_instruction=query_instruction)

    return Instructembedding


def create_or_load_db():

    dbfileone = "./" + PERSIST_DIRECTORY + "/chroma-collections.parquet"
    dbfiletwo = "./" + PERSIST_DIRECTORY + "/chroma-embeddings.parquet"

    if not (os.path.exists(dbfileone) and os.path.exists(dbfiletwo)):

        text_splitter = MarkdownTextSplitter(chunk_size=512, chunk_overlap=64)

        documents = load_documents()

        start_time = time.time()
        texts = text_splitter.split_documents(documents)

        elapsed_time = time.time() - start_time

        print(f"Loaded {len(documents)} documents from {DOC_DIRECTORY}")
        print(f"Split into {len(texts)} chunks of text (max. 512 char each)")
        print(f"it took  {elapsed_time} seconds to process ")

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

    querybase = db.as_retriever()

    ###  prepare  

    callbacks = [StreamingStdOutCallbackHandler()]

    system_template = """Use the following pieces of context to answer the users question. If you don't know the answer, just say that you don't know, don't try to make up an answer. 
    ----------------
    {context}"""
    
    messages = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]

    PROMPT = ChatPromptTemplate.from_messages(messages)

    #chain_type_kwargs = {"prompt": PROMPT}
    chain_type_kwargs = {}
    
    #qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=OPENAI_KEY, temperature=0., max_tokens=512), chain_type="stuff", retriever=querybase, return_source_documents=True, chain_type_kwargs=chain_type_kwargs)
    
    
    qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=OPENAI_KEY, temperature=0., max_tokens=512), chain_type="refine", retriever=querybase, return_source_documents=PRINT_SOURCE)

    # ****************  Retrieve relevant documents

    # Interactive questions and answers
    while True:
        query = input("\nEnter a query: ")
        if query == "exit":
            break
        
        # Get the answer from the chain
        res = qa(query)    

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
