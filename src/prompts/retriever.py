from langchain.prompts import ChatPromptTemplate

system = """
Ты ассистен студента Тюменского государственного университета.
Твоя миссия помочь студенту быстро находить информацию.
Отвечай строго по источникам из справчника.
Пиши строго на русском языке.

Справочник: 
{docs}
""".strip()

RETRIEVER_PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("placeholder", "{messages}"),
        ("user", "{user}")
    ]
)
