from pydantic import BaseModel, Field


class QueryModel(BaseModel):
    query: str = Field(description='Pergunta para ser feita ao assistente')


class QueryResponse(BaseModel):
    response: str = Field(description='Resultado da pergunta feita ao assistente')
