import os
from dotenv import load_dotenv


# ****************  Load Environemnt
load_dotenv()

## database
DOC_DIRECTORY = os.environ.get("DOC_DIRECTORY")

## embeddings parameter  >> instructor model : https://arxiv.org/pdf/2212.09741.pdf
INSTRUCT_MODEL=os.environ.get("INSTRUCT_MODEL")
CHUNK_SIZE=int(os.environ.get("CHUNK_SIZE"))
OVERLAP = 120
PERSIST_DIRECTORY = os.environ.get("PERSIST_DIRECTORY")
INTERACTIVEMODE=(os.getenv('INTERACTIVEMODE', 'False') == 'True') #false unless it is True , spelled like this 

## llm and API key 
LLMTYPE=os.environ.get("LLMTYPE")
MODEL_PATH=os.environ.get("MODEL_PATH")
OPENAI_KEY = os.environ.get("OPENAI_KEY")
PROMPTLAYER_API_KEY=os.environ.get("PROMPTLAYER_API_KEY")
PROMPTFILE=os.environ.get("PROMPTFILE")
PROMPTFILEHYDE=os.environ.get("PROMPTFILEHYDE")
QATYPE=os.environ.get("QATYPE")

## parameters  False unless excplicitly set to True 
PRINT_SOURCE = (os.getenv('PRINT_SOURCE', 'False') == 'True')
BUILD_REFRESH_DB = (os.getenv('BUILD_REFRESH_DB', 'False') == 'True')

thequery="Should we be afraid of AI ?"