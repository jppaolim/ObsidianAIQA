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
