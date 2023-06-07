from llama_index.readers.schema.base import Document
from llama_index.readers.file.markdown_reader import MarkdownReader
from typing import Any, Dict, List, Optional, Tuple, cast
import os
import sys
import logging
from pathlib import Path
from llama_index import     ObsidianReader

from langchain.embeddings import HuggingFaceInstructEmbeddings
from config import *


def embeddings_function():
    embed_instruction = "Represent the Wikipedia document for retrieval: "
    query_instruction = "Represent the Wikipedia question for retrieving supporting documents : "
    Instructembedding = HuggingFaceInstructEmbeddings(
        model_name=INSTRUCT_MODEL, embed_instruction=embed_instruction, query_instruction=query_instruction)


    return Instructembedding


def read_str_prompt(filepath: str):

    with open(filepath, 'r') as file:
            template = file.read()

    return(template) 


# custom class to add filename as doc_id et extra info d'ailleurs

class MyObsidianReader(ObsidianReader):
  def load_data(self, *args: Any, **load_kwargs: Any) -> List[Document]:
        """Load data from the input directory."""
        docs: List[Document] = []
        for dirpath, dirnames, filenames in os.walk(self.input_dir):
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            for filename in filenames:
                if filename.endswith(".md"):
                    filepath = os.path.join(dirpath, filename)
                    #remove the extrainfo
                    content = MyMDreader().load_data(Path(filepath))
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

