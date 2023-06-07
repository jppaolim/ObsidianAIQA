thequery = "Should we be afraid of AI ?"

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

from langchain.llms import  LlamaCpp

from llama_index.indices.document_summary import DocumentSummaryIndex
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.document_summary import DocumentSummaryIndexEmbeddingRetriever

from llama_index.retrievers import TreeSelectLeafEmbeddingRetriever
from llama_index.query_engine import RetrieverQueryEngine


# ****************  Load local var and utils
from config import *
from utils import read_str_prompt, MyObsidianReader, logger, embeddings_function


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
        prompt_helper=PromptHelper(context_window=2048-150,   num_output=MAXTOKEN, chunk_overlap_ratio=0.1),
        chunk_size=CHUNK_SIZE_LLAMAINDEX, 
        node_parser=SimpleNodeParser(SentenceSplitter(chunk_size=CHUNK_SIZE_LLAMAINDEX, chunk_overlap=OVERLAP))  
        )
    
    summary_template = Prompt(read_str_prompt(PROMPTSUMMARY))
    summary_templatebis = Prompt(read_str_prompt("./Prompts/LamaIndex-CustomSummaryPromptDocu.txt"))
    qa_template = Prompt(read_str_prompt(PROMPTFILEQA))
    re_template = Prompt(read_str_prompt(PROMPTFILEREFINE))
    
    documents = MyObsidianReader(DOC_DIRECTORY).load_data()
    
       
    llm.temperature=0.3
    response_synthesizer = ResponseSynthesizer.from_args(
        response_mode="tree_summarize",
        #verbose=True,
        #bug 
        text_qa_template=summary_templatebis,
        #refine_template=re_template,
        service_context=service_context
    )

    docfile  = "./storage/docstore.json" 
    indexfile = "./storage/index_store.json"
    missingfile = not (os.path.exists(docfile) and os.path.exists(indexfile))

    #if something missing or "force build", we start from scratch 
    if (missingfile or FORCE_REBUILD):
        #todo : rm dir existing 
        storage_context = StorageContext.from_defaults()
        storage_context.docstore.add_documents(documents)
        index_summary = DocumentSummaryIndex.from_documents(documents, storage_context=storage_context, service_context=service_context, response_synthesizer=response_synthesizer, summary_query=summary_template)
        #index_summary = DocumentSummaryIndex.from_documents(documents, storage_context=storage_context, service_context=service_context, summary_query=summary_template)
        
        index_summary.set_index_id = "summary"
        index_summary.storage_context.persist(persist_dir="./storage") 

    #if we have something we refresh 
    else:
        storage_context = StorageContext.from_defaults(persist_dir="./storage")
        index_summary = load_index_from_storage(storage_context, service_context=service_context, index_id="summary")
        index_summary.refresh(documents,
            update_kwargs={"delete_kwargs": {'delete_from_docstore': True}}
            )

    retriever = DocumentSummaryIndexEmbeddingRetriever(
        index=index_summary,
        similarity_top_k=4,
        #verbose=True
    )      

    llm.temperature=0.6
    response_synthesizer = ResponseSynthesizer.from_args(
        response_mode="tree_summarize",
        #verbose=True,
        text_qa_template=qa_template,
        refine_template=re_template,
        service_context=service_context
    )


    query_engine = RetrieverQueryEngine(   
        retriever=retriever,
        response_synthesizer=response_synthesizer,
    )

    
    response  = query_engine.query(thequery)

    print(response)

if __name__ == "__main__":
    main()