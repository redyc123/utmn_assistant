from vectorstore.chroma import VectorStore, Doc
from langchain.schema.runnable import RunnableParallel, RunnableLambda


class DB:
    def __init__(self, stores: list[VectorStore]):
        self.chromas = {
            store.store._collection_name: store
            for store in stores
        } if stores else {}

    async def create_chroma(self, name: str, docs: list[Doc]):
        self.chromas[name] = VectorStore(name)
        try:
            await self.chromas[name].add_docs(docs)
            return True
        except:
            return False

    async def solve(self, query):
        tasks = {
            name: RunnableLambda(vectorstore.get_docs)
            for name, vectorstore in self.chromas.items()
        }
        results = await RunnableParallel(tasks).ainvoke(query)
        return "\n\n".join([r for _, r in results.items()])
