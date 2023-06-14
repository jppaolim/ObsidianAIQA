import os
import logging
import sys
import shutil
import argparse


from llama_index import (
    VectorStoreIndex,
    ListIndex,
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

from llama_index.node_parser.simple import SimpleNodeParser
from llama_index.langchain_helpers.text_splitter import SentenceSplitter

from langchain.llms import  LlamaCpp

from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine
#from llama_index.indices.document_summary import DocumentSummaryIndexEmbeddingRetriever

from llama_index.logger import LlamaLogger
from llama_index.callbacks import CallbackManager, LlamaDebugHandler, CBEventType




# ****************  Load local var and utils
from config import *
from utils import read_str_prompt, embeddings_function

  
    
# *************** MAIN LOOP 

def main(thequery: str):

    # ***************  logging and Callback 

    logger = logging.getLogger()
    logger.setLevel(LOGLEVEL)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    #stdout_handler = logging.StreamHandler(sys.stdout)
    #stdout_handler.setLevel(logging.INFO)
    #stdout_handler.setFormatter(formatter)

    file_handler = logging.FileHandler('ouput.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    #logger.addHandler(stdout_handler)

    llama_debug = LlamaDebugHandler(print_trace_on_end=True)
    callback_manager = CallbackManager([llama_debug])
    llama_logger = LlamaLogger()


    # ***************  Embedding
    embed_model = LangchainEmbedding(embeddings_function())

    # ***************  LLM     
    
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

    # ***************  Service Context 
    #   
    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor,
        embed_model=embed_model,
        prompt_helper=PromptHelper(context_window=2048-150,   num_output=MAXTOKEN, chunk_overlap_ratio=0.1),
        chunk_size=CHUNK_SIZE, 
        node_parser=SimpleNodeParser(SentenceSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=OVERLAP,))  ,
        llama_logger=llama_logger,
        callback_manager=callback_manager
        )
    
    from llama_index import set_global_service_context
    set_global_service_context(service_context) 
        
    # ***************  Load Documents, Build Index 
           
    docfile  = PERSIST_DIRECTORY+"/docstore.json" 
    indexfile = PERSIST_DIRECTORY+"/index_store.json"
    missingfile = not (os.path.exists(docfile) and os.path.exists(indexfile))

    from llama_index import  SimpleDirectoryReader

    documents = SimpleDirectoryReader(input_dir=DOC_DIRECTORY, recursive=True, filename_as_id=True).load_data()
    #documents = MyObsidianReader(DOC_DIRECTORY).load_data()



    #if something missing or "force build", we start from scratch 
    if (missingfile or FORCE_REBUILD):
 
        if os.path.exists(PERSIST_DIRECTORY):
            shutil.rmtree(PERSIST_DIRECTORY)
        storage_context = StorageContext.from_defaults()
        storage_context.docstore.add_documents(documents)
 
        index_vec = VectorStoreIndex.from_documents(documents, storage_context=storage_context, service_context=service_context)
       
        index_vec.set_index_id("Vector")
        index_vec.storage_context.persist(persist_dir=PERSIST_DIRECTORY) 
      
    #if we have something we refresh 
    else:
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIRECTORY)
        index_vec = load_index_from_storage(storage_context, index_id="Vector", service_context=service_context) 
        
        index_vec.refresh_ref_docs(documents,
            update_kwargs={"delete_kwargs": {'delete_from_docstore': True}}
        )
        index_vec.storage_context.persist(persist_dir=PERSIST_DIRECTORY) 


    # ***************  Make the query with the real good templates 

    qa_template = Prompt(read_str_prompt(PROMPTFILEQA))
    re_template = Prompt(read_str_prompt(PROMPTFILEREFINE))

    #retrevied_nodes = get_retrieved_nodes(thequery, index_vec, service_context, vector_top_k=5, with_reranker=False)
    #visualize_retrieved_nodes(retrevied_nodes)

    #query_engine=build_queryengine(index_vec,qa_template,re_template,service_context)

    from llama_index.indices.postprocessor import PrevNextNodePostprocessor
 
    docstore=storage_context.docstore
    node_postprocessor = PrevNextNodePostprocessor (docstore=docstore, num_nodes=1, mode="both")

    retriever = VectorIndexRetriever (
        index=index_vec,
        similarity_top_k=6,

    )   

    #increase temperature and make a synthesis of the 4 documents
    if not FAKELLM: service_context.llm_predictor.llm.temperature=0.6
    response_synthesizer = ResponseSynthesizer.from_args(
        response_mode="tree_summarize",
        use_async=False,
        verbose=True,
        text_qa_template=qa_template,
        refine_template=re_template,
        service_context=service_context,
        response_kwargs={'num_children': 2},
        node_postprocessors=[node_postprocessor]

    )


    query_engine = RetrieverQueryEngine(   
        retriever=retriever,
        response_synthesizer=response_synthesizer,
    )

    
    #query_engine = index_vec.as_query_engine(   
    #    similarity_top_k=4,
    #    node_postprocessors=[node_postprocessor],
    #    use_async=False,
    #    text_qa_template=qa_template,
    #    refine_template=re_template,
    #    response_kwargs={'num_children': 3},
    #    response_mode="tree_summarize"
    #)


    response  = query_engine.query(thequery)
    print(response)


    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-query", type=str, required=True, help="Query string to process")
    args = parser.parse_args()
    main(args.query)