from langchain.docstore.document import Document
from config import PRINT_SOURCE

def build_string_context(context: list[Document]):
    inputcontext = ""
    
    if PRINT_SOURCE: 
        print(f"Context for {query} : ")
        print("\n")

    for doc in context:
        if PRINT_SOURCE: 
            print(doc)
            print("\n")
        inputcontext = inputcontext + doc.page_content + "\n"  
    return inputcontext
