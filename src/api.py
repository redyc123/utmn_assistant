import asyncio
import os
from typing import Literal, TypedDict
from llm.mistral import mistral
from vectorstore.db import DB, Doc
from prompts.retriever import RETRIEVER_PROMPT

db = DB([])


class GPTMessage(TypedDict):
    role: Literal["user", "assistant"]
    content: str


async def chatting(messages: list[GPTMessage]):
    chain = RETRIEVER_PROMPT | mistral
    user = messages.pop(-1)
    docs = []
    async for t in chain.astream({"docs": docs, "messages": messages, "user": user}):
        yield t


async def main():
    await db.create_chroma(
        "Literature",
        [Doc(
            name="Коллекции Пушкина", author="А.С. Пушкин",
            text="У лукоморья дуб Зеленый"
        )]
    )
    async for t in chatting([{"role": "user", "content": "привет"}]):
        print(t, end="")

asyncio.run(main())
