import os
import logging
import sys


from llama_index import (
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

from llama_index.indices.document_summary import GPTDocumentSummaryIndex
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.document_summary import DocumentSummaryIndexEmbeddingRetriever

# ****************  Load local var and utils
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
#    insert_prompt = Prompt(read_str_prompt(PROMPTINSERT))
    qa_template = Prompt(read_str_prompt(PROMPTFILEQA))
    re_template = Prompt(read_str_prompt(PROMPTFILEREFINE))
#    select_template = Prompt(read_str_prompt(PROMPTSELECT))
#    select_template_multiple = Prompt(read_str_prompt(PROMPTSELECTMULTIPLE))


    response_synthesizer = ResponseSynthesizer.from_args(
        response_mode="tree_summarize",
        verbose=True,
        text_qa_template=qa_template,
        refine_template=re_template,
        service_context=service_context
    )
        
    if BUILD_REFRESH_DB:
        documents = ObsidianReader(DOC_DIRECTORY).load_data()
        storage_context = StorageContext.from_defaults()
        storage_context.docstore.add_documents(documents)
        
        index = GPTDocumentSummaryIndex.from_documents(documents, storage_context=storage_context, service_context=service_context, response_synthesizer=response_synthesizer, summary_query=summary_template)
        index.storage_context.persist(persist_dir="./storage") 

    else:
        storage_context = StorageContext.from_defaults(persist_dir="./storage")
        index = load_index_from_storage(storage_context, service_context=service_context)



    retriever = DocumentSummaryIndexEmbeddingRetriever(
        index=index,
        similarity_top_k=4,
        verbose=True
        # choice_select_prompt=choice_select_prompt,
        # choice_batch_size=choice_batch_size,
        # format_node_batch_fn=format_node_batch_fn,
        # parse_choice_select_answer_fn=parse_choice_select_answer_fn,
        # service_context=service_context
    )

    #response_synthesizer = ResponseSynthesizer.from_args(
    #    response_mode="refine",
    #    verbose=True,
    #    text_qa_template=qa_template,
    #    refine_template=re_template,
    #    service_context=service_context
    #)
  
    

    query_engine = RetrieverQueryEngine(
        
        retriever=retriever,
        response_synthesizer=response_synthesizer,
#        query_template=select_template,
#        query_template_multiple = select_template_multiple,
#        service_context=service_context
    )


    response  = query_engine.query("Can you build a moat with AI while everybody uses the same big model ?")

    print(response)

if __name__ == "__main__":
    main()

