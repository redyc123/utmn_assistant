from typing import Literal, TypedDict
from llm.mistral import mistral
from vectorstore.db import DB, Doc
from prompts.retriever import RETRIEVER_PROMPT
from uuid import uuid1

db = DB([])


class GPTMessage(TypedDict):
    role: Literal["user", "assistant"]
    content: str


async def chatting(messages: list[GPTMessage]):
    chain = RETRIEVER_PROMPT | mistral
    user = messages.pop(-1)
    docs = await db.solve(user)
    async for t in chain.astream({"docs": docs, "messages": messages, "user": user}):
        yield t


async def add_text(author: str, text: str):
    name = str(uuid1())
    docs = [Doc(name=name, author=author, text=t) for t in text.split("\n\n")]
    db.create_chroma(name=name, docs=docs)
    return "Тексты успешно добавлены."
