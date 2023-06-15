import os
import logging

from dotenv import load_dotenv
load_dotenv()


## SRC DOC
#DOC_DIRECTORY = "../RessourcesDummy"
DOC_DIRECTORY = "../Ressources"

## STORAGE
PERSIST_DIRECTORY="./db"

## embeddings parameter  >> instructor model : https://arxiv.org/pdf/2212.09741.pdf
INSTRUCT_MODEL="hkunlp/instructor-large"
#needed for HF 
TOKENIZERS_PARALLELISM=False
CHUNK_SIZE=800
#MAXTOKEN = 384
MAXTOKEN = 512
OVERLAP = 20

## llm 
OPENAI_KEY=os.environ.get("OPENAI_KEY")
PROMPTLAYER_API_KEY=os.environ.get("PROMPTLAYER_API_KEY")
MODEL="gpt-3.5-turbo"
BASE_MODELPATH="../models/"
#MODEL_PATH=BASE_MODELPATH + "Wizard-Vicuna-7B-Uncensored.ggmlv3.q5_1.bin"
MODEL_PATH=BASE_MODELPATH + "WizardLM-13B-1.0.ggmlv3.q4_0.bin" 

## PROMTPS
BASE_PROMPTPATH="./Prompts/"
PROMPTFILEQA=BASE_PROMPTPATH + "Base.txt"
PROMPTFILEREFINE=BASE_PROMPTPATH + "Refine.txt"
#PROMPTSUMMARY=BASE_PROMPTPATH + "Summary.txt"
#PROMPTSUMMARYDOC=BASE_PROMPTPATH + "SummaryDoc.txt"
#PROMPTSUMMARYDOCREFINE=BASE_PROMPTPATH + "SummaryDocRefine.txt"
#PROMPTRANK=BASE_PROMPTPATH + "Rerank.txt"


## Behavior 
LOGLEVEL=logging.DEBUG

#rebuild database 
FORCE_REBUILD= False
#BUILD_REFRESH_DB=false

#test with fake LLM 
FAKELLM=False

###useless
INTERACTIVEMODE=False
RUNVANILLA=True
LLMTYPE="LLAMACPP"
QATYPE="Manual"
PROMPTFILE="./Prompts/customLLAMA.txt"
PRINT_SOURCE=False