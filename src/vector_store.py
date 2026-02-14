import faiss
import numpy as np
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

endpoint = "https://models.github.ai/inference"

client = OpenAI(
    base_url=endpoint,
    api_key=token
)

class VectorStore:

    def __init__(self):
        self.index = None
        self.chunks = []

    def create_embeddings(self, chunks):

        embeddings = []

        for chunk in chunks:

            response = client.embeddings.create(
                model="text-embedding-3-small",   # Try this first
                input=chunk
            )

            embeddings.append(response.data[0].embedding)

        return np.array(embeddings).astype("float32")

    def build_index(self, chunks):

        self.chunks = chunks

        embeddings = self.create_embeddings(chunks)

        dim = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def search(self, query, k=3):

        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=query
        )

        query_vector = np.array([response.data[0].embedding]).astype("float32")

        distances, indices = self.index.search(query_vector, k)

        return [self.chunks[i] for i in indices[0]]
