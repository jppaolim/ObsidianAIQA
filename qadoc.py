import os
import re
import requests
import time


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

# ****************  Interact

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
        PLChat = PromptLayerChatOpenAI(openai_api_key=OPENAI_KEY, temperature=0.1, max_tokens=2048, verbose=True)

        PROMPT=customize_prompt(PROMPTFILE) 
        chain_type_kwargs = {"prompt": PROMPT} 
        chain = RetrievalQA.from_chain_type(llm=PLChat, chain_type="stuff", retriever=dbretriever, chain_type_kwargs=chain_type_kwargs)
        res = chain(thequery)
        answer  = res['result']  
        print(answer)
        
    elif LLMTYPE=="LLAMACPP-AUTOQA":

        dbretriever = db.as_retriever(search_type="mmr", search_kwargs={"k":5, "lambda_mult":0.9})
        llamamodel = LlamaCpp(model_path=MODEL_PATH, n_threads=6,  n_ctx=2048, max_tokens=400,  temperature = 0.8, top_k = 50, top_p=0.9, verbose=True, use_mlock=True)
        
        PROMPT=customize_prompt(PROMPTFILE) 
        chain_type_kwargs = {"prompt": PROMPT} 
        chain = RetrievalQA.from_chain_type(llm=llamamodel, chain_type="stuff",  retriever=dbretriever, chain_type_kwargs=chain_type_kwargs)
                
    elif LLMTYPE=="LLAMACPP-MANUAL":

        dbretriever = db.as_retriever(search_type="mmr", search_kwargs={"k":4, "lambda_mult":0.9})
        llamamodel = LlamaCpp(model_path=MODEL_PATH, n_threads=6,  n_ctx=2048, max_tokens=500,  temperature = 0.7, top_k = 50, top_p=0.75, last_n_tokens_size=256,  n_batch=1024, echo = True, repeat_penalty=1.17647, use_mmap=True, verbose=True, use_mlock=True,  callbacks=Streamcallbacks)

        context = dbretriever.get_relevant_documents(thequery) 
        print(f"Context for {thequery} : ")
        inputcontext=build_string_context(context)
        
        PROMPT=customize_prompt(PROMPTFILE) 
        chain = LLMChain(llm=llamamodel, prompt=PROMPT) 
        inputs = [{"context": inputcontext, "question": thequery}]
 
        print(chain.apply(inputs)[0]["text"]) 
  
    elif LLMTYPE=="LLAMACPP-HYDE":
        
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
        
        PROMPT=customize_prompt(PROMPTFILE) 
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

