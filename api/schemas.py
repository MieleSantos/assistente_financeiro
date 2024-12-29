from pydantic import BaseModel, Field


class QueryModel(BaseModel):
    query: str = Field(description='Pergunta para ser feita ao assistente')
    provedor_ai: str = Field(
        description='Escolha o provedor de ai [openai,groq]', default='groq'
    )


class QueryResponse(BaseModel):
    response: str = Field(description='Resultado da(s) pergunta feita ao assistente')
