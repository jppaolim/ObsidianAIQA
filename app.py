import streamlit as st
import os
import logging
import sys


from llama_index import (
    GPTVectorStoreIndex, 
    LangchainEmbedding,
    LLMPredictor, 
    ServiceContext, 
    StorageContext, 
    load_index_from_storage,
    ObsidianReader,
    Prompt,
    PromptHelper
)

from llama_index.node_parser.simple import SimpleNodeParser
from llama_index.langchain_helpers.text_splitter import SentenceSplitter

from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.llms import  LlamaCpp


# ****************  Load local  
from config import *
from utils import read_str_prompt

# ****************  Logger

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('llamaindex.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


# ************ embeddings 

def embeddings_function():
    embed_instruction = "Represent the Wikipedia document for retrieval: "
    query_instruction = "Represent the Wikipedia question for retrieving supporting documents : "
    Instructembedding = HuggingFaceInstructEmbeddings(
        model_name=INSTRUCT_MODEL, embed_instruction=embed_instruction, query_instruction=query_instruction)

    return Instructembedding

# *************** MAIN LOOP 

@st.cache_resource
def load_everything():
    embed_model = LangchainEmbedding(embeddings_function())
    llm = LlamaCpp(model_path=MODEL_PATH, n_threads=6,  n_ctx=2048, max_tokens=512,  temperature = 0.6, top_k = 45, top_p=0.80, last_n_tokens_size=256,  n_batch=1024, repeat_penalty=1.17647, use_mmap=True, use_mlock=True)
    llm.client.verbose= False

    llm_predictor = LLMPredictor(llm=llm)
    
    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor,
        embed_model=embed_model,
        node_parser=SimpleNodeParser(text_splitter=SentenceSplitter(chunk_size=CHUNK_SIZE_LLAMAINDEX, chunk_overlap=OVERLAP)), 
        )
        
    if BUILD_REFRESH_DB:
        documents = ObsidianReader(DOC_DIRECTORY).load_data()
        storage_context = StorageContext.from_defaults()
        storage_context.docstore.add_documents(documents)
        index = GPTVectorStoreIndex.from_documents(documents, storage_context=storage_context, service_context=service_context)
        index.storage_context.persist(persist_dir="./storage")

    else:
        storage_context = StorageContext.from_defaults(persist_dir="./storage")
        index = load_index_from_storage(storage_context, service_context=service_context)

    prompt_helper = PromptHelper(context_window=2048,   num_output=512, chunk_overlap_ratio=0.1)
        
    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor,
        embed_model=embed_model,
        prompt_helper=prompt_helper,
        chunk_size=CHUNK_SIZE_LLAMAINDEX, 
        
        )

    qa_template = Prompt(read_str_prompt(PROMPTFILEQA))
    re_template = Prompt(read_str_prompt(PROMPTFILEREFINE))

    query_engine = index.as_query_engine(
        verbose=True,
        similarity_top_k=3,
        text_qa_template=qa_template,
        refine_template=re_template,
        service_context=service_context
    )


    return query_engine
    



query_engine = load_everything()


if 'response' not in st.session_state:
    st.session_state.response = ''

def send_click():
    st.session_state.response  = query_engine.query(st.session_state.prompt)

st.title("ChatJPP")

st.text_input("Ask something: ", key='prompt')
st.button("Send", on_click=send_click)
if st.session_state.response:
    st.subheader("Response: ")
    st.success(st.session_state.response, icon= "🤖")
