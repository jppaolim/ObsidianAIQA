import os
import re
import time
import requests

import pandas as pd
from dotenv import load_dotenv

from langchain.llms import OpenAI, LlamaCpp

from langchain.chat_models import PromptLayerChatOpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from langchain.prompts import PromptTemplate

from langchain.chains import RetrievalQA
from langchain.chains import LLMChain, HypotheticalDocumentEmbedder

# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# ****************  Load Environemnt

load_dotenv()

## database
DOC_DIRECTORY = os.environ.get("DOC_DIRECTORY")

## embeddings parameter  >> instructor model : https://arxiv.org/pdf/2212.09741.pdf
INSTRUCT_MODEL=os.environ.get("INSTRUCT_MODEL")
CHUNK_SIZE=int(os.environ.get("CHUNK_SIZE"))
OVERLAP = 120
PERSIST_DIRECTORY = os.environ.get("PERSIST_DIRECTORY")

## llm and API key 
LLMTYPE=os.environ.get("LLMTYPE")
MODEL_PATH=os.environ.get("MODEL_PATH")
OPENAI_KEY = os.environ.get("OPENAI_KEY")
PROMPTLAYER_API_KEY=os.environ.get("PROMPTLAYER_API_KEY")

## parameters  False unless excplicitly set to True 
PRINT_SOURCE = (os.getenv('PRINT_SOURCE', 'False') == 'True')
BUILD_REFRESH_DB = (os.getenv('BUILD_REFRESH_DB', 'False') == 'True')

query1 =  "Can we build a moat for an AI startup ?"
query2 =  "Should we be afraid of AI ?"
query3 =  "Who do you think is going to win in generative AI space ? Name the potential actors or cluster them and comment on the pros and cons."
query4 =  "Find 3 different ways to explain the difference between AI and generative AI using analogies to a college level student and without technical jargon"
thequery=query3

# ****************  Embeddings function 
from langchain.embeddings import HuggingFaceInstructEmbeddings
def embeddings_function():
    embed_instruction = "Represent the Wikipedia document for retrieval: "
    query_instruction = "Represent the Wikipedia question for retrieving supporting documents : "
    Instructembedding = HuggingFaceInstructEmbeddings(
        model_name=INSTRUCT_MODEL, embed_instruction=embed_instruction, query_instruction=query_instruction)

    return Instructembedding

# ****************  Document Loader & Vector Store 

from langchain.document_loaders import TextLoader, DirectoryLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import CharacterTextSplitter, MarkdownTextSplitter, RecursiveCharacterTextSplitter

from langchain.vectorstores import FAISS 


def create_or_load_db_faiss():

    #see if we need to build 
    faissDir = "./" + PERSIST_DIRECTORY + "/faiss_index/" 
    faissfile1 = "./" + PERSIST_DIRECTORY + "/faiss_index/index.faiss" 
    faissfile2 = "./" + PERSIST_DIRECTORY + "/faiss_index/index.pkl" 
    missingfile = not (os.path.exists(faissfile1) and os.path.exists(faissfile2))

    if (missingfile or BUILD_REFRESH_DB):
        
        if os.path.exists(faissfile1):
            os.remove(faissfile1)
        if os.path.exists(faissfile2):
            os.remove(faissfile2)

        text_splitter = MarkdownTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=OVERLAP)
        docdirectory = "./" + DOC_DIRECTORY + "/"

        loader = DirectoryLoader(
            docdirectory, glob="**/*.md", loader_cls=UnstructuredMarkdownLoader)

        documents = loader.load()
        texts = text_splitter.split_documents(documents)

        print(f"Loaded {len(documents)} documents from {DOC_DIRECTORY}")
        print(f"Split into {len(texts)} chunks of text (max. {CHUNK_SIZE} char each). Chunk distribution is as follow: ")
        textspd = pd.Series(map(lambda x:len(x.page_content), texts))
        stats = textspd.describe()
        print(stats)

        start_time = time.time()
        db = FAISS.from_documents(texts, embeddings_function())    
        #db = FAISS.from from_documents(texts, embeddings_function())    
        elapsed_time = time.time() - start_time
        print(f"it took  {elapsed_time} seconds to create the database with indicated embeddings ")
        
        db.save_local(faissDir)

    else:
        db = FAISS.load_local(faissDir, embeddings_function()) 
    
    return db 

# ****************  Prompt Custom 

def customize_chat_prompt():

    system_template = """You act as an helpful and insightful research assistant. Use you own knowledge and incorporate the most relevant points of the following context to write a nuanced, well argumented and credible anwer to the user question.
        ----------------
        {context}"""
    
    messages = [
            SystemMessagePromptTemplate.from_template(system_template),
            HumanMessagePromptTemplate.from_template("{question}"),
        ]

    PROMPT = ChatPromptTemplate.from_messages(messages)
    
    return PROMPT

def customize_LLAMA_prompt():

    prompt_template = """### Human : You act as an helpful and insightful research assistant. Use you own knowledge and incorporate the most relevant points of the following context to write a nuanced, well argumented and credible anwer to the question. Here is the context : 

    {context}

    Now is the question: {question}
    ### Assistant :"""
    PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
    )

    
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
    
    start_time = time.time()
    res = qa(query)
    elapsed_time = time.time() - start_time
  
    print("\n")
    print(f"it took  {elapsed_time} seconds to put up following answer : ")
    answer  = res['result']  
    print(answer)
    
    return


def main():

    db = create_or_load_db_faiss()



    if LLMTYPE=="ChatGPT":
        dbretriever = db.as_retriever(search_type="mmr", search_kwargs={"k":5, "lambda_mult":0.9})

        PROMPT=customize_chat_prompt() 
        chain_type_kwargs = {"prompt": PROMPT} 
        qa = RetrievalQA.from_chain_type(llm=PromptLayerChatOpenAI(openai_api_key=OPENAI_KEY, temperature=0.1, max_tokens=2048, verbose=True), chain_type="stuff", retriever=dbretriever, chain_type_kwargs=chain_type_kwargs)
        qb = RetrievalQA.from_chain_type(llm=PromptLayerChatOpenAI(openai_api_key=OPENAI_KEY, temperature=0.7, max_tokens=2048, verbose=True), chain_type="stuff", retriever=dbretriever, chain_type_kwargs=chain_type_kwargs)

    elif LLMTYPE=="LLAMACPP":
        dbretriever = db.as_retriever(search_type="mmr", search_kwargs={"k":5, "lambda_mult":0.9})

        llamamodel = LlamaCpp(model_path=MODEL_PATH, n_threads=6,  n_ctx=2048, max_tokens=400,  temperature = 0.8, top_k = 50, top_p=0.9, verbose=True, use_mlock=True)
        PROMPT=customize_LLAMA_prompt() 
        chain_type_kwargs = {"prompt": PROMPT} 
        qa = RetrievalQA.from_chain_type(llm=llamamodel, chain_type="stuff",  retriever=dbretriever, chain_type_kwargs=chain_type_kwargs)
        #qb = RetrievalQA.from_chain_type(llm=llamamodel, chain_type="stuff", retriever=querybase, chain_type_kwargs=chain_type_kwargs)

    elif LLMTYPE=="LLAMACPPV2":
        dbretriever = db.as_retriever(search_type="mmr", search_kwargs={"k":5, "lambda_mult":0.9})

        prompt_template = """### Human :You act as an insightful assistant. Use you own knowledge but incorporate the most relevant points of the following context to write a nuanced, well argumented and credible article based on the user query. In case you have no firm opinion list pros and cons. In case you have one, defend it well. Make hypothesis to produce a point of view. Avoid falsehood. Add a section about how this point of view could be wrong.
        Here is the context : 
        {context}
        Now is the query: {question}
        ### Assistant :"""

        PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

        context = dbretriever.get_relevant_documents(thequery) 
        print(f"Context for {thequery} : ")
        inputcontext = ""
        for doc in context:
            print(doc)
            print("\n")
            inputcontext = inputcontext + doc.page_content + "\n"   
        
        llamamodel = LlamaCpp(model_path=MODEL_PATH, n_threads=6,  n_ctx=2048, max_tokens=400,  temperature = 0.7, top_k = 60, top_p=0.85, verbose=True, use_mlock=True)
        
        chain = LLMChain(llm=llamamodel, prompt=PROMPT) 
 
        inputs = [{"context": inputcontext, "question": thequery}]
        print(chain.apply(inputs)[0]["text"]) 

    elif LLMTYPE=="LLAMACPPV3":
        dbretriever = db.as_retriever(search_type="mmr", search_kwargs={"k":5, "lambda_mult":0.9})

        llamamodel = LlamaCpp(model_path=MODEL_PATH, n_threads=6,  n_ctx=2048, max_tokens=400,  temperature = 0.7, top_k = 60, top_p=0.85, verbose=True, use_mlock=True)

        prompt_template = """### Human : You act as an helpful and insightful research assistant. Please write a nuanced, well argumented and credible anwer to the user question. 
        {question}
        ### Assistant :"""
        prt = PromptTemplate(input_variables=["question"], template=prompt_template)
        hydeChain = LLMChain(llm=llamamodel, prompt=prt)

        hydeEmbeddings = HypotheticalDocumentEmbedder(llm_chain=hydeChain, base_embeddings=embeddings_function())
    
        result = hydeEmbeddings.embed_query(thequery)
        context =  db.max_marginal_relevance_search_by_vector(result, k=5, lambda_mult=0.9)
        
        print(f"Context for {thequery} : ")
        inputcontext = ""
        for doc in context:
            print(doc)
            print("\n")
            inputcontext = inputcontext + doc.page_content + "\n"   
        
        PROMPT=customize_LLAMA_prompt() 
        chain = LLMChain(llm=llamamodel, prompt=PROMPT) 
   
        inputs = [{"context": inputcontext, "question": query1}]
        print(chain.apply(inputs)[0]["text"]) 
        
        
    else:
        raise SystemExit("Mistake in LLM")

    #go_and_answer(query1, qa)
    
    db = None
    exit

if __name__ == "__main__":
    main()

