import asyncio
from langchain_chroma import Chroma
from embedding.mistral import mistral_emb_model
from langchain_core.documents import Document
from pydantic import BaseModel


class Doc(BaseModel):
    name: str
    author: str
    text: str
    metadata: dict = {}


def docs_to_strings(docs: list[Document]):
    texts = [
        f"{d.page_content}\n\nИсточнк: {d.metadata['name']} Автор: {d.metadata['author']}"
        for d in docs
    ]
    return texts


class VectorStore:
    def __init__(self, collection_name: str):
        self.collection_name = collection_name
        self.store = Chroma(collection_name, mistral_emb_model)

    async def add_docs(self, docs: list[Doc]):
        documents = [
            Document(d.text, metadata={
                "author": d.author,
                "name": d.name,
                **d.metadata,
            })
            for d in docs
        ]
        await self.store.aadd_documents(documents)
        await asyncio.sleep(1.1)

    async def get_docs(self, query: str):
        docs = await self.store.asimilarity_search(query)
        await asyncio.sleep(1.2)
        return docs_to_strings(docs)
