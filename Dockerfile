FROM python:3.11-slim

WORKDIR /srv

COPY ./src /srv

RUN pip install langchain langchain-chroma langchain-mistralai aiogram

CMD ["python", "srv.py"]