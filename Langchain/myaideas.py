import os
#import re
#import requests

#from dotenv import load_dotenv

from langchain.llms import  LlamaCpp

from langchain.chat_models import PromptLayerChatOpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from langchain.prompts import PromptTemplate
from langchain.vectorstores import VectorStore

from langchain.chains import RetrievalQA
from langchain.chains import LLMChain, HypotheticalDocumentEmbedder

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
Streamcallbacks = [StreamingStdOutCallbackHandler()]


# ****************  Load everything 
from config import *
from embed import embeddings_function, create_or_load_db_faiss
from utils import build_string_context


# ****************  Prompt Custom 

def customize_prompt(filepath):

    if LLMTYPE=="ChatGPT": 
    
        with open(filepath, 'r') as file:
                system_template = file.read()

        messages = [
                SystemMessagePromptTemplate.from_template(system_template),
                HumanMessagePromptTemplate.from_template("{question}"),
            ]

        PROMPT = ChatPromptTemplate.from_messages(messages)
    
    else:    
        with open(filepath, 'r') as file:
                prompt_template = file.read()

        PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
        )
            
    return PROMPT

# ****************  Build Inputs from query 

def build_inputs(query : str, dbretriever : VectorStore):
     
    if LLMTYPE=="ChatGPT": inputsdict = {"query": query}

    elif LLMTYPE=="LLAMACPP": 
 
        if QATYPE =="AUTO": 
            inputsdict = {"query": query}
        elif QATYPE=="MANUAL":   
            context = dbretriever.get_relevant_documents(query)       
            inputcontext=build_string_context(context)
            inputsdict = {"context": inputcontext, "question": query}
        else:
            raise SystemExit("No corresponding QATYPE")
    else:
        raise SystemExit("Mistake in LLM")
    return inputsdict


def main():

    db = create_or_load_db_faiss()
    dbretriever = db.as_retriever(search_type="mmr", search_kwargs={"k":4, "lambda_mult":0.9})

    PROMPT=customize_prompt(PROMPTFILE) 
    chain_type_kwargs = {"prompt": PROMPT} 



    
    if LLMTYPE=="ChatGPT":
        
        theLLM = PromptLayerChatOpenAI(openai_api_key=OPENAI_KEY, temperature=0.1, max_tokens=2048, verbose=False, streaming=True, callbacks=[StreamingStdOutCallbackHandler()])
        chain = RetrievalQA.from_chain_type(llm=theLLM, chain_type="stuff", retriever=dbretriever, chain_type_kwargs=chain_type_kwargs)
             
    elif LLMTYPE=="LLAMACPP": 

        theLLM = LlamaCpp(model_path=MODEL_PATH, n_threads=6,  n_ctx=2048, max_tokens=500,  temperature = 0.7, top_k = 50, top_p=0.75, last_n_tokens_size=256,  n_batch=1024, echo = True, repeat_penalty=1.17647, use_mmap=True, verbose=True, use_mlock=True,  callbacks=Streamcallbacks)
        theLLM.client.verbose = False

        if QATYPE =="AUTO": chain = RetrievalQA.from_chain_type(llm=theLLM, chain_type="stuff",  retriever=dbretriever, chain_type_kwargs=chain_type_kwargs)
        elif QATYPE=="MANUAL": chain = LLMChain(llm=theLLM, prompt=PROMPT) 
        else: raise SystemExit("No corresponding QATYPE")  
    else: raise SystemExit("Mistake in LLM")

    if RUNVANILLA: 
        with open(PROMPTFILEHYDE, 'r') as file:
            prt = file.read()
        PRT = PromptTemplate(template=prt, input_variables=["question"])
        vanillachain = LLMChain(llm=theLLM, prompt=PRT)
    
    if INTERACTIVEMODE:
        while True:
            query = input("\nEnter a query: ")
            if query == "exit":
                break
            inputsdict=build_inputs(query, dbretriever)
            res= chain(inputsdict,return_only_outputs=True)
            if RUNVANILLA: 
                print("\nVanilla mode: \n")
                vanillachain(query, return_only_outputs=True)

    else:
        inputsdict=build_inputs(thequery, dbretriever)
        res= chain(inputsdict,return_only_outputs=True)

    db = None
    exit

if __name__ == "__main__":
    main()

