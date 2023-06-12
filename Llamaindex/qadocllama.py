thequery = "Gen AI systems are hard to control. Here are top ideas to still use them in a reliable way."

import os
import logging
import sys
import shutil

from llama_index import (
    #VectorStoreIndex,
    #TreeIndex,
    DocumentSummaryIndex,
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
from langchain.llms.fake import FakeListLLM 
    

from llama_index.logger import LlamaLogger

from llama_index.node_parser.simple import SimpleNodeParser
from llama_index.langchain_helpers.text_splitter import SentenceSplitter

from langchain.llms import  LlamaCpp

from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.document_summary import DocumentSummaryIndexEmbeddingRetriever

from llama_index.callbacks import CallbackManager, LlamaDebugHandler, CBEventType


# ****************  Load local var and utils
from config import *
from utils import read_str_prompt, MyObsidianReader, logger, embeddings_function


# *************** Query engine 

def build_queryengine(index_summary: DocumentSummaryIndex, qa_template:str, re_template:str, service_context:ServiceContext ):
        
        #retriever to get top 4 relevant documents
        retriever = DocumentSummaryIndexEmbeddingRetriever(
            index=index_summary,
            similarity_top_k=4,
        )      

        #increase temperature and make a synthesis of the 4 documents
        if not FAKELLM: service_context.llm_predictor.llm.temperature=0.6
        response_synthesizer = ResponseSynthesizer.from_args(
            response_mode="tree_summarize",
            use_async=False,
            text_qa_template=qa_template,
            refine_template=re_template,
            service_context=service_context
        )

        query_engine = RetrieverQueryEngine(   
            retriever=retriever,
            response_synthesizer=response_synthesizer,
        )

        return query_engine



# *************** MAIN LOOP 

def main():

    embed_model = LangchainEmbedding(embeddings_function())

    # ***************  load LLLM     
    
    if not FAKELLM:
        llm = LlamaCpp(model_path=MODEL_PATH, n_threads=6,  n_ctx=2048, max_tokens=MAXTOKEN,  temperature = 0.3, top_k = 45, top_p=0.80, last_n_tokens_size=256,  n_batch=1024, repeat_penalty=1.17647, use_mmap=True, use_mlock=True)
        llm.client.verbose= False
    else :
        responses=[
        "This is a great summary 1",
        "This is a great summary 2",
        "This is a great summary 3",
        "This is a great summary 4",
        "This is a great summary 5" ,
        "This is a great summary 6",
        "This is a great summary 7",
        "This is a great summary 8"
        ]

        llm = FakeListLLM(responses=responses)

    llm_predictor = LLMPredictor(llm=llm)

    llama_debug = LlamaDebugHandler(print_trace_on_end=True)
    callback_manager = CallbackManager([llama_debug])

    llama_logger = LlamaLogger()


    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor,
        embed_model=embed_model,
        prompt_helper=PromptHelper(context_window=2048-150,   num_output=MAXTOKEN, chunk_overlap_ratio=0.1),
        chunk_size=CHUNK_SIZE_LLAMAINDEX, 
        node_parser=SimpleNodeParser(SentenceSplitter(chunk_size=CHUNK_SIZE_LLAMAINDEX, chunk_overlap=OVERLAP))  ,
        llama_logger=llama_logger,
        callback_manager=callback_manager
        )
    
        
    # ***************  Load Documents, Build Index 
           
    DocBuildResponse_synthesizer = ResponseSynthesizer.from_args(
        response_mode="tree_summarize",
        #important locally to not use async 
        use_async=False,
        #bug it uses text_qa_template to generate summary 
        text_qa_template=Prompt(read_str_prompt(PROMPTSUMMARYDOC)),
        refine_template=Prompt(read_str_prompt(PROMPTSUMMARYDOCREFINE)),
        service_context=service_context
    )

    docfile  = "./storage/docstore.json" 
    indexfile = "./storage/index_store.json"
    missingfile = not (os.path.exists(docfile) and os.path.exists(indexfile))

    documents = MyObsidianReader(DOC_DIRECTORY).load_data()

    #if something missing or "force build", we start from scratch 
    if (missingfile or FORCE_REBUILD):
 
        if os.path.exists("./storage"):
            shutil.rmtree("./storage")
        storage_context = StorageContext.from_defaults()
        storage_context.docstore.add_documents(documents)
 
        index_summary = DocumentSummaryIndex.from_documents(documents, storage_context=storage_context, service_context=service_context,
            response_synthesizer=DocBuildResponse_synthesizer,summary_query=Prompt(read_str_prompt(PROMPTSUMMARYDOC)) )
       
        index_summary.set_index_id("ObsidianSummary")
        index_summary.storage_context.persist(persist_dir="./storage") 
      
    #if we have something we refresh 
    else:
        storage_context = StorageContext.from_defaults(persist_dir="./storage")
        index_summary = load_index_from_storage(storage_context, index_id="ObsidianSummary", service_context=service_context, response_synthesizer=DocBuildResponse_synthesizer,summary_query=Prompt(read_str_prompt(PROMPTSUMMARYDOC))) 
        
                 #index_summary.refresh_ref_docs(documents,
        #    update_kwargs={"delete_kwargs": {'delete_from_docstore': True}}
        #)
        #index_summary.storage_context.persist(persist_dir="./storage") 


    # ***************  Make the query with the real good templates 

    qa_template = Prompt(read_str_prompt(PROMPTFILEQA))
    re_template = Prompt(read_str_prompt(PROMPTFILEREFINE))

    query_engine=build_queryengine(index_summary,qa_template,re_template,service_context)

    response  = query_engine.query(thequery)
    print(response)
    
    
if __name__ == "__main__":
    main()