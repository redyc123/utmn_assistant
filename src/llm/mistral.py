from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.output_parsers import StrOutputParser

mistral = ChatMistralAI(
    name="mistral-large-latest",
    streaming=True
) | StrOutputParser()
