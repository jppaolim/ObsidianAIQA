import os
#import re
#import requests

#from dotenv import load_dotenv

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


def main():

    db = create_or_load_db_faiss()
    PROMPT=customize_prompt(PROMPTFILE) 
    chain_type_kwargs = {"prompt": PROMPT} 


    if LLMTYPE=="ChatGPT":
        
        dbretriever = db.as_retriever(search_type="mmr", search_kwargs={"k":5, "lambda_mult":0.9})
        PLChat = PromptLayerChatOpenAI(openai_api_key=OPENAI_KEY, temperature=0.1, max_tokens=2048, verbose=True, streaming=True, callbacks=[StreamingStdOutCallbackHandler()])

        inputsdict = {"query": thequery}
        chain = RetrievalQA.from_chain_type(llm=PLChat, chain_type="stuff", retriever=dbretriever, chain_type_kwargs=chain_type_kwargs)

                
    elif LLMTYPE=="LLAMACPP": 

        dbretriever = db.as_retriever(search_type="mmr", search_kwargs={"k":4, "lambda_mult":0.9})
        llamamodel = LlamaCpp(model_path=MODEL_PATH, n_threads=6,  n_ctx=2048, max_tokens=1000,  temperature = 0.7, top_k = 50, top_p=0.75, last_n_tokens_size=256,  n_batch=1024, echo = True, repeat_penalty=1.17647, use_mmap=True, verbose=True, use_mlock=True,  callbacks=Streamcallbacks)
   
        if QATYPE =="AUTO":

            inputsdict = {"query": thequery}
            chain = RetrievalQA.from_chain_type(llm=llamamodel, chain_type="stuff",  retriever=dbretriever, chain_type_kwargs = {"prompt": PROMPT} )

        elif QATYPE=="MANUAL":
      
            context = dbretriever.get_relevant_documents(thequery)       
            print(f"Context for {thequery} : ")
            inputcontext=build_string_context(context)

            inputsdict = {"context": inputcontext, "question": thequery}
            chain = LLMChain(llm=llamamodel, prompt=PROMPT) 

        elif QATYPE=="HYDE":

            print("HYDE vanilla generation :")
            with open(PROMPTFILEHYDE, 'r') as file:
                prt = file.read()
            PRT = PromptTemplate(template=prt, input_variables=["question"])
            hydeChain = LLMChain(llm=llamamodel, prompt=PRT)
            hydeEmbeddings = HypotheticalDocumentEmbedder(llm_chain=hydeChain, base_embeddings=embeddings_function())     
            result = hydeEmbeddings.embed_query(thequery)


            context =  db.max_marginal_relevance_search_by_vector(result, k=4, lambda_mult=0.9)
            print(f"Context for {thequery} : ")
            inputcontext=build_string_context(context)
            
            inputsdict = {"context": inputcontext, "question": thequery}
            chain = LLMChain(llm=llamamodel, prompt=PROMPT) 
        
        else:
            raise SystemExit("No corresponding QATYPE")
        
    else:
        raise SystemExit("Mistake in LLM")


    res= chain(inputsdict,return_only_outputs=True)

    #go_and_answer(query1, qa)
    
    db = None
    exit

if __name__ == "__main__":
    main()

