from fastapi import APIRouter, Body, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from api.assistent.assistents import search_assistent
from api.schemas import QueryModel, QueryResponse

router = APIRouter()
templates = Jinja2Templates(directory='templates')

chat_history = []


@router.get('/', response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        'index.html', {'request': request, 'message_received': None}
    )


@router.post('/send-message/', response_class=HTMLResponse)
async def send_message(request: Request):
    data = await request.form()

    user_msg = data.get('message')
    chat_history.append({'sender': 'user', 'text': user_msg})

    response = search_assistent(question=user_msg, provedor_ai='openai')
    chat_history.append({'sender': 'bot', 'text': response})

    return templates.TemplateResponse(
        'index.html', {'request': request, 'chat_history': chat_history}
    )


@router.post(
    '/seach',
    status_code=status.HTTP_200_OK,
    response_model=QueryResponse,
    description='Search agente',
)
async def search_agent(query: QueryModel = Body(...)) -> QueryResponse:
    if query.query:
        return search_assistent(query.query, query.provedor_ai)
