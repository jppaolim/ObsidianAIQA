import os
from dotenv import load_dotenv
load_dotenv()

## SRC DOC
DOC_DIRECTORY = os.environ.get("DOC_DIRECTORY")

## embeddings parameter  >> instructor model : https://arxiv.org/pdf/2212.09741.pdf
INSTRUCT_MODEL=os.environ.get("INSTRUCT_MODEL")
CHUNK_SIZE_LLAMAINDEX=int(os.environ.get("CHUNK_SIZE_LLAMAINDEX"))
OVERLAP = 120

## llm and prompt 
MODEL_PATH=os.environ.get("MODEL_PATH")
PROMPTFILEQA=os.environ.get("PROMPTFILEQA")
PROMPTFILEREFINE=os.environ.get("PROMPTFILEREFINE")
QATYPE=os.environ.get("QATYPE")

## parameters False unless excplicitly set to True 
BUILD_REFRESH_DB = (os.getenv('BUILD_REFRESH_DB', 'False') == 'True')
INTERACTIVEMODE=(os.getenv('INTERACTIVEMODE', 'False') == 'True') 
RUNVANILLA=(os.getenv('RUNVANILLA', 'False') == 'True') 