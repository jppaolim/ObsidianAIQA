thequery = "How a company can create competitive advantage with generative AI if everybody uses the same big model ?"

import os
import logging
import sys


from llama_index import (
    VectorStoreIndex,
    TreeIndex,
    LangchainEmbedding,
    LLMPredictor, 
    ServiceContext, 
    StorageContext, 
    load_index_from_storage,
    ObsidianReader,
    Prompt,
    ResponseSynthesizer,
    PromptHelper
)


from llama_index.node_parser.simple import SimpleNodeParser
from llama_index.langchain_helpers.text_splitter import SentenceSplitter

from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.llms import  LlamaCpp

from llama_index.indices.document_summary import DocumentSummaryIndex
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.document_summary import DocumentSummaryIndexEmbeddingRetriever

from llama_index.retrievers import TreeSelectLeafEmbeddingRetriever
from llama_index.query_engine import RetrieverQueryEngine


# ****************  Load local var and utils
from config import *
from utils import read_str_prompt, MyObsidianReader

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

def main():

    MAXTOKEN = 384

    embed_model = LangchainEmbedding(embeddings_function())
        
    # llm = LlamaCpp(model_path=MODEL_PATH, n_threads=6,  n_ctx=2048, max_tokens=500,  temperature = 0.7, top_k = 50, top_p=0.75, last_n_tokens_size=256,  n_batch=1024, echo = True, repeat_penalty=1.17647, use_mmap=True, verbose=True, use_mlock=True,  callbacks=Streamcallbacks)
    llm = LlamaCpp(model_path=MODEL_PATH, n_threads=6,  n_ctx=2048, max_tokens=MAXTOKEN,  temperature = 0.6, top_k = 45, top_p=0.80, last_n_tokens_size=256,  n_batch=1024, repeat_penalty=1.17647, use_mmap=True, use_mlock=True)
    llm.client.verbose= False

    llm_predictor = LLMPredictor(llm=llm)

    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor,
        embed_model=embed_model,
        prompt_helper=PromptHelper(context_window=2048-100,   num_output=MAXTOKEN, chunk_overlap_ratio=0.1),
        chunk_size=CHUNK_SIZE_LLAMAINDEX, 
        node_parser=SimpleNodeParser(SentenceSplitter(chunk_size=CHUNK_SIZE_LLAMAINDEX, chunk_overlap=OVERLAP))  
        )
    
    
    summary_template = Prompt(read_str_prompt(PROMPTSUMMARY))
    insert_prompt = Prompt(read_str_prompt(PROMPTINSERT))
    qa_template = Prompt(read_str_prompt(PROMPTFILEQA))
    re_template = Prompt(read_str_prompt(PROMPTFILEREFINE))
    select_template = Prompt(read_str_prompt(PROMPTSELECT))
    select_template_multiple = Prompt(read_str_prompt(PROMPTSELECTMULTIPLE))

    if BUILD_REFRESH_DB:
        documents = MyObsidianReader(DOC_DIRECTORY).load_data()
        storage_context = StorageContext.from_defaults()
        storage_context.docstore.add_documents(documents)
        #nodes = node_parser.get_nodes_from_documents(documents)
        #storage_context.persist(persist_dir="./storage")
    else:
        storage_context = StorageContext.from_defaults(persist_dir="./storage")
    
    
    if QATYPE=="SUMMARY":

        response_synthesizer = ResponseSynthesizer.from_args(
            response_mode="tree_summarize",
            #verbose=True,
            text_qa_template=qa_template,
            refine_template=re_template,
            service_context=service_context
        )

        if BUILD_REFRESH_DB:
            index_summary = DocumentSummaryIndex.from_documents(documents, storage_context=storage_context, service_context=service_context, response_synthesizer=response_synthesizer, summary_query=summary_template)
            index_summary.set_index_id = "summary"
            index_summary.storage_context.persist(persist_dir="./storage") 

        else:
            index_summary = load_index_from_storage(storage_context, service_context=service_context, index_id="summary")

        retriever = DocumentSummaryIndexEmbeddingRetriever(
            index=index_summary,
            similarity_top_k=4,
            #verbose=True
        )      

        query_engine = RetrieverQueryEngine(   
            retriever=retriever,
            response_synthesizer=response_synthesizer,
        )

    elif QATYPE=="TREE":
        if BUILD_REFRESH_DB:
            index_tree = TreeIndex.from_documents(documents, storage_context=storage_context, service_context=service_context, summary_template=summary_template , insert_prompt=insert_prompt)
            index_tree.set_index_id = "tree"
            index_tree.storage_context.persist(persist_dir="./storage") 

        else:
            index_tree = load_index_from_storage(storage_context, service_context=service_context, index_id="tree")
   
        retriever = TreeSelectLeafEmbeddingRetriever(
            index=index_tree,
            child_branch_factor=4,
            query_template=select_template,
            query_template_multiple = select_template_multiple,
            #verbose=True,
            service_context=service_context
        )

        response_synthesizer = ResponseSynthesizer.from_args(
            #verbose==True,
            text_qa_template=qa_template,
            refine_template=re_template,
            service_context=service_context
        )

        query_engine = RetrieverQueryEngine(
            retriever=retriever,
            response_synthesizer=response_synthesizer
        )
     

    elif QATYPE=="VECTOR":
        if BUILD_REFRESH_DB:
            index = VectorStoreIndex.from_documents(documents, storage_context=storage_context, service_context=service_context)
            index.set_index_id = "vector"
            index.storage_context.persist(persist_dir="./storage") 

        else:
            index = load_index_from_storage(storage_context, service_context=service_context, index_id="vector")

        query_engine = index.as_query_engine(
            #verbose=True,
            similarity_top_k=4,
            text_qa_template=qa_template,
            refine_template=re_template,
            service_context=service_context
        )

    response  = query_engine.query(thequery)

    print(response)

if __name__ == "__main__":
    main()