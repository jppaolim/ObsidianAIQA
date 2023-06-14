
DS UTILS / 
import time

def create_custom_uuid():
    # Get the current time in milliseconds
    timestamp = int(time.time()*1000)

    # Convert it to hexadecimal
    timestamp_hex = hex(timestamp)[2:]

    # Generate a random UUID
    random_uuid = uuid.uuid4().hex

    # Combine the timestamp with the random UUID, and insert hyphens
    # to make it look like a typical UUID
    custom_uuid = timestamp_hex + random_uuid[len(timestamp_hex):]
    custom_uuid = '-'.join([custom_uuid[i:i+4] for i in range(0, len(custom_uuid), 4)])

    return custom_uuid


#def get_new_id(d: Set) -> str:
#    """Get a new ID."""
#    while True:
#        new_id = str(uuid.uuid4())
#        if new_id not in d:
#            break
#    return new_id


def get_new_id(d: Set) -> str:
    """Get a new ID."""
    while True:
        new_id = str(create_custom_uuid())
        if new_id not in d:
            break
    return new_id



DS /opt/homebrew/Caskroom/miniforge/base/envs/ObsidianAIQA/lib/python3.10/site-packages/llama_index/indices/postprocessor/node.py 
        sorted_nodes = sorted(all_nodes.values(), key=lambda x: x.node.get_doc_id(), reverse=True)




CE QUIO CHANGE C'EST DOC SUMMARY INDEX  base.py

    def __init__(
        self,
        nodes: Optional[Sequence[Node]] = None,
        index_struct: Optional[IndexDocumentSummary] = None,
        service_context: Optional[ServiceContext] = None,
        response_synthesizer: Optional[ResponseSynthesizer] = None,
        summary_query: str = DEFAULT_SUMMARY_QUERY,
        **kwargs: Any,
    ) -> None:
        """Initialize params."""
        self._response_synthesizer = (
            response_synthesizer
            or ResponseSynthesizer.from_args(service_context=service_context)
        )
        self._summary_query = summary_query or "summarize:"
        super().__init__(
            nodes=nodes,
            index_struct=index_struct,
            service_context=service_context,
            response_synthesizer=response_synthesizer,
            **kwargs,
        )



class TreeSummarize(Refine):
    def __init__(
        self,
        service_context: ServiceContext,
        text_qa_template: QuestionAnswerPrompt,
        refine_template: RefinePrompt,
        streaming: bool = False,
        use_async: bool = True,
    ) -> None:
        super().__init__(
            service_context=service_context,
            text_qa_template=text_qa_template,
            refine_template=refine_template,
            streaming=streaming,
        )
        self._use_async = use_async



    @classmethod
    def from_documents(
        cls: Type[IndexType],
        documents: Sequence[Document],
        storage_context: Optional[StorageContext] = None,
        service_context: Optional[ServiceContext] = None,
        response_synthesizer: Optional[ResponseSynthesizer] = None,
        **kwargs: Any,
    ) -> IndexType:
        """Create index from documents.

        Args:
            documents (Optional[Sequence[BaseDocument]]): List of documents to
                build the index from.

        """
        storage_context = storage_context or StorageContext.from_defaults()
        service_context = service_context or ServiceContext.from_defaults()
        docstore = storage_context.docstore

        with service_context.callback_manager.as_trace("index_construction"):
            for doc in documents:
                docstore.set_document_hash(doc.get_doc_id(), doc.get_doc_hash())

            nodes = service_context.node_parser.get_nodes_from_documents(documents)

            return cls(
                nodes=nodes,
                storage_context=storage_context,
                service_context=service_context,
                response_synthesizer=response_synthesizer,
                **kwargs,
                )


from langchain.llms.fake import FakeListLLM 
    responses=[
    "This is a great summary 1",
    "This is a great summary 2",
    "This is a great summary 3",
    "This is a great summary 4",
    "This is a great summary 5" ,
    "This is a great summary 6",
    "This is a great summary 7",
    "This is a great summary 8"
    ]

    llm = FakeListLLM(responses=responses)



from collections import defaultdict

from llama_index.data_structs.document_summary import IndexDocumentSummary
from llama_index.data_structs.node import DocumentRelationship, Node, NodeWithScore
from llama_index.indices.query.response_synthesis import ResponseSynthesizer
from llama_index.indices.service_context import ServiceContext


from llama_index.data_structs.data_structs import IndexStruct

#IS = TypeVar("IS", bound=IndexStruct)
IndexType = TypeVar("IndexType", bound="MyDocumentSummaryIndex")

class MyDocumentSummaryIndex(DocumentSummaryIndex):
    """Document Summary Index.

    Args:
        summary_template (Optional[SummaryPrompt]): A Summary Prompt
            (see :ref:`Prompt-Templates`).

    """
    def __init__(
        self,
        nodes: Optional[Sequence[Node]] = None,
        index_struct: Optional[IndexDocumentSummary] = None,
        service_context: Optional[ServiceContext] = None,
        response_synthesizer: Optional[ResponseSynthesizer] = None,
        #I change it here ... 
        summary_query: Optional[str] =  summarydoc,
        **kwargs: Any,
    ) -> None:
        """Initialize params."""
        self._response_synthesizer = (
            response_synthesizer
            or ResponseSynthesizer.from_args(service_context=service_context)
        )
        #I change it here ... 
        #self._summary_query = summarydoc 
        #print(summary_query)
        super().__init__(
            nodes=nodes,
            index_struct=index_struct,
            service_context=service_context,
            response_synthesizer=response_synthesizer,
            summary_query=summary_query,
            **kwargs,
        )



# custom Doc Reader class to add filename as doc_id et extra info d'ailleurs
from llama_index import     ObsidianReader
from llama_index.readers.schema.base import Document
from llama_index.readers.file.markdown_reader import MarkdownReader
from typing import Any, Dict, List, Optional, Tuple, cast, Sequence, Type, TypeVar

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
        for idx, tup in enumerate(tups):
          header=tup[0]
          value = tup[1]
          if header is None:
            results.append(Document(value, doc_id= f"{str(file)}_part_{idx}",extra_info=extra_info))
        else:
            results.append(
                Document(f"\n\n{header}\n{value}", doc_id=f"{str(file)}_part_{idx}", extra_info=extra_info)
            )
        return results