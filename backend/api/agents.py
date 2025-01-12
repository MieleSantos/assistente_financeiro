from fastapi import APIRouter, Body, status

from api.assistent.assistents import search_assistent
from api.schemas import QueryModel, QueryResponse

router = APIRouter()

chat_history = []


@router.post(
    '/seach',
    status_code=status.HTTP_200_OK,
    response_model=QueryResponse,
    description='Search agente',
)
async def search_agent(query: QueryModel = Body(...)) -> QueryResponse:
    if query.query:
        resp = search_assistent(query.query, query.provedor_ai)
        print(resp)
        return resp
