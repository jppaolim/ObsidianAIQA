from llama_index.readers.schema.base import Document
from llama_index.readers.file.markdown_reader import MarkdownReader
from typing import Any, Dict, List, Optional, Tuple, cast
import os
from pathlib import Path
from llama_index import     ObsidianReader



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


