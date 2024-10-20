from pydantic import BaseModel, Field


class QueryModel(BaseModel):
    query: str = Field(description='Pergunta para ser feita ao assistente')
