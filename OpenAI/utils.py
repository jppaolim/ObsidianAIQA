import os
import sys

from config import *


#set up embedding INSTRUCTOR 
from langchain.embeddings import HuggingFaceInstructEmbeddings

def embeddings_function():
    embed_instruction = "Represent the Wikipedia document for retrieval: "
    query_instruction = "Represent the Wikipedia question for retrieving supporting documents : "
    Instructembedding = HuggingFaceInstructEmbeddings(
        model_name=INSTRUCT_MODEL, embed_instruction=embed_instruction, query_instruction=query_instruction)
    return Instructembedding


#Utility to read the prompts 
from pathlib import Path

def read_str_prompt(filepath: str):

    with open(filepath, 'r') as file:
            template = file.read()

    return(template) 
#summarydoc=read_str_prompt(PROMPTSUMMARYDOC)



from llama_index.indices.postprocessor import (
    LLMRerank
)
from llama_index.indices.query.schema import QueryBundle
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
    Prompt
    )
from llama_index.retrievers import VectorIndexRetriever


def get_retrieved_nodes(query_str:str, index: VectorStoreIndex, service_context: ServiceContext, vector_top_k=10, reranker_top_n=2, with_reranker=False):
    query_bundle = QueryBundle(query_str)
    # configure retriever
    retriever = VectorIndexRetriever(
        index=index, 
        similarity_top_k=vector_top_k,
    )
    retrieved_nodes = retriever.retrieve(query_bundle)

    if with_reranker:
        # configure reranker
        reranker = LLMRerank(choice_batch_size=2, top_n=reranker_top_n, service_context=service_context, choice_select_prompt=Prompt(read_str_prompt(PROMPTRANK)))
        retrieved_nodes = reranker.postprocess_nodes(retrieved_nodes, query_bundle)
    
    return retrieved_nodes


def visualize_retrieved_nodes(nodes) -> None:
    result_dicts = []
    for node in nodes:
        print(f'\n\n****Score****: {node.score}\n****Node text****\n: {node.node.get_text()}'
        )
    #    result_dict = {
    #        "Score": node.score,
    #        "Text": node.node.get_text()
    #    }
    #    result_dicts.append(result_dict)
        
    #pretty_print(pd.DataFrame(result_dicts))