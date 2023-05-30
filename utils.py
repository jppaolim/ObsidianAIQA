from langchain.docstore.document import Document

def build_string_context(context: list[Document]):
    inputcontext = ""
    for doc in context:
        print(doc)
        print("\n")
        inputcontext = inputcontext + doc.page_content + "\n"  
    return inputcontext

