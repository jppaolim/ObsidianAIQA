import os
import re
import time
import requests

import pandas as pd

from dotenv import load_dotenv

from langchain.document_loaders import TextLoader, DirectoryLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import CharacterTextSplitter, MarkdownTextSplitter, RecursiveCharacterTextSplitter


from langchain.vectorstores import Chroma, FAISS 

from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.vectorstores.base import VectorStoreRetriever
 

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

from langchain.chat_models import PromptLayerChatOpenAI
from langchain.chat_models import ChatOpenAI

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# ****************  Load Environemnt

load_dotenv()

LLM = os.environ.get("MODEL")
OPENAI_KEY = os.environ.get("OPENAI_KEY")
PROMPTLAYER_API_KEY=os.environ.get("PROMPTLAYER_API_KEY")
PERSIST_DIRECTORY = os.environ.get("PERSIST_DIRECTORY")
DOC_DIRECTORY = os.environ.get("DOC_DIRECTORY")
PRINT_SOURCE = False
INSTRUCT_MODEL=os.environ.get("INSTRUCT_MODEL")
### instructor model is trained on 512 token so roughly up to 2K character. So setting at 1500 we should be good.
# then if we pass 4 documents to the chain it should be OK.   
CHUNK_SIZE=int(os.environ.get("CHUNK_SIZE"))
OVERLAP = 16

BUILD_REFRESH_DB=os.environ.get("BUILD_REFRESH_DB")

# **************** Load embeddings

#instructor model : https://arxiv.org/pdf/2212.09741.pdf
from langchain.embeddings import HuggingFaceInstructEmbeddings

def embeddings_function():
    embed_instruction = "Represent the Wikipedia document for retrieval: "
    query_instruction = "Represent the Wikipedia question for retrieving supporting documents : "
    Instructembedding = HuggingFaceInstructEmbeddings(
        model_name=INSTRUCT_MODEL, embed_instruction=embed_instruction, query_instruction=query_instruction)

    return Instructembedding

# ****************  Document Loader

def load_documents():
    docdirectory = "./" + DOC_DIRECTORY + "/"

    loader = DirectoryLoader(
        docdirectory, glob="**/*.md", loader_cls=UnstructuredMarkdownLoader)
    return loader.load()

def create_or_load_db_chroma():

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
    
    db.persist()

    return db 

def create_or_load_db_faiss():
    faissfile = "./" + PERSIST_DIRECTORY + "/faiss_index" 

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

    if not (os.path.exists(faissfile)):


        start_time = time.time()
        
        db = FAISS.from_documents(texts, embeddings_function())
        
        elapsed_time = time.time() - start_time
        print(f"it took  {elapsed_time} seconds to create the database with indicated embeddings ")
        
        db.save_local(faissfile)
    else:
        db = FAISS.load_local(faissfile, embeddings_function()) 
    
    return db 

def customize_prompt():

    system_template = """You act as an helpful and insightful research assistant. Use you own knowledge and incorporate the most relevant points of the following context to write a nuanced, well argumented and credible anwer to the user question.
        ----------------
        {context}"""
    
    messages = [
            SystemMessagePromptTemplate.from_template(system_template),
            HumanMessagePromptTemplate.from_template("{question}"),
        ]

    PROMPT = ChatPromptTemplate.from_messages(messages)
    
    return PROMPT

def go_and_interact(qa : RetrievalQA):

    # Interactive questions and answers
    while True:

        query = input("\nEnter a query: ")
        if query == "exit":
            break
        
        res = qa(query)
        #qa.run(query)    

        if PRINT_SOURCE:
             answer, docs = res['result'], res['source_documents']
        else:
            answer  = res['result']  

        print(answer)
        
        if PRINT_SOURCE:
            # Print the relevant sources used for the answer
            for document in docs:
                print("\n> " + document.metadata["source"] + ":")
                print(document.page_content)

    return

def go_and_answer(query: str, qa : RetrievalQA):
    res = qa(query)
    answer  = res['result']  
    print(answer)
    print("\n")
    
    return

def go_and_getrelevantDocs(querybase :  VectorStoreRetriever, query : str):
    relevantDocs =querybase.get_relevant_documents(query)
    for rdoc in relevantDocs:
        print("-------------------------------")
        print(rdoc.page_content)
        print("\n")
    return

def main():

    db = create_or_load_db_faiss()

    querybase = db.as_retriever(search_type="mmr", search_kwargs={"k":4, "lambda_mult":0.7})


    PROMPT=customize_prompt() 

    chain_type_kwargs = {"prompt": PROMPT} 
    qa = RetrievalQA.from_chain_type(llm=PromptLayerChatOpenAI(openai_api_key=OPENAI_KEY, temperature=0.1, max_tokens=2048, verbose=True), chain_type="stuff", retriever=querybase, chain_type_kwargs=chain_type_kwargs)

    qb = RetrievalQA.from_chain_type(llm=PromptLayerChatOpenAI(openai_api_key=OPENAI_KEY, temperature=0.7, max_tokens=2048, verbose=True), chain_type="stuff", retriever=querybase, chain_type_kwargs=chain_type_kwargs)

    #pour aller interagir
    #go_and_interact(qa)   

    #ou pr répondre à la question
    go_and_answer("Should we be afraid of AI ?", qa)
    go_and_answer("Should we be afraid of AI ?", qb)
   
    go_and_answer("Please build a scenario of how an AI could take over the world. Brainstorm about mitigation tactics.", qa)
    go_and_answer("Please build a scenario of how an AI could take over the world. Brainstorm about mitigation tactics.", qb)
   
    db = None
    exit

# Not used anymoore
def unusedcode():
    #db = create_or_load_db_chroma()
    #querybase = db.as_retriever(search_type="similarity", search_kwargs={"k":3})

    #callbacks = [StreamingStdOutCallbackHandler()]

    #go_and_getrelevantDocs(querybase, "Who is Geoffrey hilton")
    #go_and_getrelevantDocs(querybase, "should we be afraid of AI ?")

    #qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=OPENAI_KEY, temperature=0., max_tokens=512), chain_type="refine", retriever=querybase, return_source_documents=PRINT_SOURCE)
    #qa = RetrievalQA.from_chain_type(llm=PromptLayerChatOpenAI(openai_api_key=OPENAI_KEY, temperature=0.1, max_tokens=2048, verbose=True), chain_type="stuff", retriever=querybase, return_source_documents=True, verbose = True, chain_type_kwargs=chain_type_kwargs)

    return


if __name__ == "__main__":
    main()

