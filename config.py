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
PROMPTSUMMARY=os.environ.get("PROMPTSUMMARY")
PROMPTINSERT=os.environ.get("PROMPTINSERT")
PROMPTSELECT=os.environ.get("PROMPTSELECT")
PROMPTSELECTMULTIPLE=os.environ.get("PROMPTSELECTMULTIPLE")
QATYPE=os.environ.get("QATYPE")

## parameters False unless excplicitly set to True 
BUILD_REFRESH_DB = (os.getenv('BUILD_REFRESH_DB', 'False') == 'True')
BUILD_TREE = (os.getenv('BUILD_TREE', 'False') == 'True')
INTERACTIVEMODE=(os.getenv('INTERACTIVEMODE', 'False') == 'True') 
RUNVANILLA=(os.getenv('RUNVANILLA', 'False') == 'True') 