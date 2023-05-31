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

query1 =  "Can we build a moat for an AI startup ?"
query2 =  "Should we be afraid of AI ?"
query3 =  "Who do you think is going to win in generative AI space ? Do you believe it will be a big tech incumbent like Google, or a startup ?"
query4 =  "Find 3 different ways to explain the difference between AI and generative AI using analogies to a college level student and without technical jargon"
query5 =  "I would like to understand how I could use generative AI in my company, what could be the use cases. I work in a FMCG company producing cosmetics."
query6 =  "As a big corporate traditional company, should we launch an AI app asap or wait for the market to be more mature ?"

thequery=query6
