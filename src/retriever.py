from src.vector_store import VectorStore
from src.log_chunker import chunk_log


class LogRetriever:

    def __init__(self, log_text):
        self.vector_store = VectorStore()

        chunks = chunk_log(log_text)

        self.vector_store.build_index(chunks)

    def get_relevant_chunks(self, question):

        return self.vector_store.search(question)
