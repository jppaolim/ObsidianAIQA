import os
from dotenv import load_dotenv
load_dotenv()

## SRC DOC
DOC_DIRECTORY = os.environ.get("DOC_DIRECTORY")

## embeddings parameter  >> instructor model : https://arxiv.org/pdf/2212.09741.pdf
INSTRUCT_MODEL=os.environ.get("INSTRUCT_MODEL")
CHUNK_SIZE_LLAMAINDEX=int(os.environ.get("CHUNK_SIZE_LLAMAINDEX"))
#MAXTOKEN = 384
MAXTOKEN = 512
OVERLAP = 20

## llm and prompt 
MODEL_PATH=os.environ.get("MODEL_PATH")
PROMPTFILEQA=os.environ.get("PROMPTFILEQA")
PROMPTFILEREFINE=os.environ.get("PROMPTFILEREFINE")
PROMPTSUMMARY=os.environ.get("PROMPTSUMMARY")
PROMPTSUMMARYDOC=os.environ.get("PROMPTSUMMARYDOC")
PROMPTSUMMARYDOCREFINE=os.environ.get("PROMPTSUMMARYDOCREFINE")



## parameters False unless excplicitly set to True 
FORCE_REBUILD= (os.getenv('FORCE_REBUILD', 'False') == 'True')
FAKELLM=(os.getenv('FAKELLM', 'False') == 'True') 


###useless
INTERACTIVEMODE=(os.getenv('INTERACTIVEMODE', 'False') == 'True') 
RUNVANILLA=(os.getenv('RUNVANILLA', 'False') == 'True') 
QATYPE=os.environ.get("QATYPE")
