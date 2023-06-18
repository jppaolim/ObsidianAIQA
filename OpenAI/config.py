import os
import logging

from dotenv import load_dotenv
load_dotenv()


## SRC DOC
#DOC_DIRECTORY = "../RessourcesDummy"
DOC_DIRECTORY = "../Ressources"

## STORAGE
PERSIST_DIRECTORY="./db"

CHUNK_SIZE=2000
MAXTOKEN = 2000
OVERLAP = 100 

## llm 
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")
PROMPTLAYER_API_KEY=os.environ.get("PROMPTLAYER_API_KEY")
MODEL="gpt-3.5-turbo"
BASE_MODELPATH="../models/"

## PROMTPS
BASE_PROMPTPATH="./Prompts/"
PROMPTFILEQA=BASE_PROMPTPATH + "Base.txt"
PROMPTFILEREFINE=BASE_PROMPTPATH + "Refine.txt"


## Behavior 
LOGLEVEL=logging.DEBUG

#rebuild database 
FORCE_REBUILD= False

#test with fake LLM 
FAKELLM=False