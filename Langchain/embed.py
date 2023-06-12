from config import *
import pandas as pd
import time

from langchain.document_loaders import TextLoader, DirectoryLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import CharacterTextSplitter, MarkdownTextSplitter, RecursiveCharacterTextSplitter

from langchain.vectorstores import FAISS 

from langchain.embeddings import HuggingFaceInstructEmbeddings

def embeddings_function():
    embed_instruction = "Represent the Wikipedia document for retrieval: "
    query_instruction = "Represent the Wikipedia question for retrieving supporting documents : "
    Instructembedding = HuggingFaceInstructEmbeddings(
        model_name=INSTRUCT_MODEL, embed_instruction=embed_instruction, query_instruction=query_instruction)

    return Instructembedding

def create_or_load_db_faiss():

    #see if we need to build 
    faissDir = "./" + PERSIST_DIRECTORY + "/faiss_index/" 
    faissfile1 = "./" + PERSIST_DIRECTORY + "/faiss_index/index.faiss" 
    faissfile2 = "./" + PERSIST_DIRECTORY + "/faiss_index/index.pkl" 
    missingfile = not (os.path.exists(faissfile1) and os.path.exists(faissfile2))

    if (missingfile or BUILD_REFRESH_DB):
        
        if os.path.exists(faissfile1):
            os.remove(faissfile1)
        if os.path.exists(faissfile2):
            os.remove(faissfile2)

        text_splitter = MarkdownTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=OVERLAP)
        docdirectory = "./" + DOC_DIRECTORY + "/"

        loader = DirectoryLoader(
            docdirectory, glob="**/*.md", loader_cls=UnstructuredMarkdownLoader)

        documents = loader.load()
        texts = text_splitter.split_documents(documents)

        print(f"Loaded {len(documents)} documents from {DOC_DIRECTORY}")
        print(f"Split into {len(texts)} chunks of text (max. {CHUNK_SIZE} char each). Chunk distribution is as follow: ")
        textspd = pd.Series(map(lambda x:len(x.page_content), texts))
        stats = textspd.describe()
        print(stats)

        start_time = time.time()
        db = FAISS.from_documents(texts, embeddings_function())    
        #db = FAISS.from from_documents(texts, embeddings_function())    
        elapsed_time = time.time() - start_time
        print(f"it took  {elapsed_time} seconds to create the database with indicated embeddings ")
        
        db.save_local(faissDir)

    else:
        db = FAISS.load_local(faissDir, embeddings_function()) 
    
    return db 