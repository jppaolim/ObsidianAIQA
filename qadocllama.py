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

from llama_index.prompts.prompt_type import PromptType



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
        service_context.llm_predictor.llm.temperature=0.6
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
    llm = LlamaCpp(model_path=MODEL_PATH, n_threads=6,  n_ctx=2048, max_tokens=MAXTOKEN,  temperature = 0.3, top_k = 45, top_p=0.80, last_n_tokens_size=256,  n_batch=1024, repeat_penalty=1.17647, use_mmap=True, use_mlock=True)
    llm.client.verbose= False
    llm_predictor = LLMPredictor(llm=llm)

    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor,
        embed_model=embed_model,
        prompt_helper=PromptHelper(context_window=2048-150,   num_output=MAXTOKEN, chunk_overlap_ratio=0.1),
        chunk_size=CHUNK_SIZE_LLAMAINDEX, 
        node_parser=SimpleNodeParser(SentenceSplitter(chunk_size=CHUNK_SIZE_LLAMAINDEX, chunk_overlap=OVERLAP))  
        )
    
    
    
    # ***************  Build Prompts  for summary  
    #initial creation use summary template or NOT 
    #summary_template = Prompt(read_str_prompt(PROMPTSUMMARY))
        
  

    #bug it uses text_qa_template to generate summary while it should be something else    
    #for creation time this will hack the process 
    DEFAULT_SUMMARY_QUERY =""
    DEFAULT_TEXT_QA_PROMPT = Prompt(read_str_prompt(PROMPTSUMMARYDOC))
    DEFAULT_REFINE_PROMPT = Prompt(read_str_prompt(PROMPTSUMMARYDOCREFINE))

    #summary4docs = Prompt(read_str_prompt(PROMPTSUMMARYDOC))

    
    # ***************  Load Documents, Build Index 
    documents = MyObsidianReader(DOC_DIRECTORY).load_data()
           
    response_synthesizer = ResponseSynthesizer.from_args(
        response_mode="tree_summarize",
        #important locally to not use async 
        use_async=False,
        #bug it uses text_qa_template to generate summary 
        #text_qa_template=summary4docs,
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
        #index_summary = DocumentSummaryIndex.from_documents(documents, storage_context=storage_context, service_context=service_context, response_synthesizer=response_synthesizer, summary_query=summary_template)
        index_summary = DocumentSummaryIndex.from_documents(documents, storage_context=storage_context, service_context=service_context, response_synthesizer=response_synthesizer)
        index_summary.storage_context.persist(persist_dir="./storage") 

    #if we have something we refresh 
    #warning when refreshing it uses default_qa_prompt template .... 
    else:
        storage_context = StorageContext.from_defaults(persist_dir="./storage")
        index_summary = load_index_from_storage(storage_context, service_context=service_context)
        index_summary.refresh_ref_docs(documents, response_synthesizer=response_synthesizer,
            update_kwargs={"delete_kwargs": {'delete_from_docstore': True}}
            )


    # ***************  Make the query with the real good templates 

    qa_template = Prompt(read_str_prompt(PROMPTFILEQA))
    re_template = Prompt(read_str_prompt(PROMPTFILEREFINE))

    #retrieved_nodes=retriever.retrieve(thequery)
    #print(len(retrieved_nodes))

    query_engine=build_queryengine(index_summary,qa_template,re_template,service_context)

    response  = query_engine.query(thequery)
    print(response)
    
    
if __name__ == "__main__":
    main()