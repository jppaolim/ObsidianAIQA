import os
import logging
import sys

from typing import Any, Dict, List, Optional, Tuple, cast


from pathlib import Path
from typing import Any, List

from llama_index import (
    ServiceContext, 
    StorageContext, 
    load_index_from_storage,
    ObsidianReader
)

from llama_index.utils import globals_helper
from llama_index.readers.schema.base import Document
from llama_index.readers.file.markdown_reader import MarkdownReader

from llama_index.node_parser.simple import SimpleNodeParser
from llama_index.langchain_helpers.text_splitter import SentenceSplitter

from langchain.text_splitter import  RecursiveCharacterTextSplitter, MarkdownTextSplitter



# ****************  Load local var and utils
from config import *


# ****************  Logger

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('llamaindex.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


# custom class 

# il va prendre tous les .md et les mettre sous les différents headers 
class MyObsidianReader(ObsidianReader):
  def load_data(self, *args: Any, **load_kwargs: Any) -> List[Document]:
        """Load data from the input directory."""
        docs: List[Document] = []
        for dirpath, dirnames, filenames in os.walk(self.input_dir):
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            for filename in filenames:
                if filename.endswith(".md"):
                    filepath = os.path.join(dirpath, filename)
                    content = MyMDreader().load_data(Path(filepath),extra_info={"filename": filepath})
                    docs.extend(content)
        return docs

class MyMDreader(MarkdownReader):
    def load_data(
        self, file: Path, extra_info: Optional[Dict] = None
    ) -> List[Document]:
        """Parse file into string."""
        tups = self.parse_tups(file)
        results = []
        # TODO: don't include headers right now
        for header, value in tups:
            if header is None:
                results.append(Document(value, doc_id= str(file),extra_info=extra_info))
            else:
                results.append(
                    Document(f"\n\n{header}\n{value}", doc_id= str(file), extra_info=extra_info)
                )
        return results


# *************** MAIN LOOP 

def main():

    node_parser1=SimpleNodeParser(SentenceSplitter(chunk_size=CHUNK_SIZE_LLAMAINDEX, chunk_overlap=OVERLAP)) 
    node_parser2=SimpleNodeParser(MarkdownTextSplitter(chunk_size=CHUNK_SIZE_LLAMAINDEX, chunk_overlap=OVERLAP)) 
   

    documents = MyObsidianReader(DOC_DIRECTORY).load_data()
    storage_context = StorageContext.from_defaults()
    storage_context.docstore.add_documents(documents)

    nodes1 = node_parser1.get_nodes_from_documents(documents)
    nodes2 = node_parser2.get_nodes_from_documents(documents)

    
    #storage_context.persist(persist_dir="./storage")

    with open('documents_1.txt', 'w') as f:
        for idx, doc in enumerate(documents):
              #f.write("\n-------\n\n{}. Size: {} tokens\n".format(idx, len(tokenizer(doc.text))) + doc.text + doc.extra_info_str)
                f.write(str(doc.to_dict()))
    print(len(documents))

    with open('splitting_1.txt', 'w') as f:
        for idx, doc in enumerate(nodes1):
            #f.write("\n-------\n\n{}. Size: {} tokens\n".format(idx, len(tokenizer(doc.text))) + doc.text)
            f.write(str(doc.to_dict()))
    print(len(nodes1))

    with open('splitting_2.txt', 'w') as f:
        for idx, doc in enumerate(nodes2):
            #f.write("\n-------\n\n{}. Size: {} tokens\n".format(idx, len(tokenizer(doc.text))) + doc.text)
            f.write(str(doc.to_dict()))
    print(len(nodes2))


if __name__ == "__main__":
    main()