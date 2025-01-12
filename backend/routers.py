from fastapi import APIRouter

from api.agents import router as search_agente

api_router = APIRouter()
api_router.include_router(search_agente, prefix='/assistent', tags=['Assistente'])
