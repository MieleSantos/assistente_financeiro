import uvicorn
from fastapi import FastAPI

from routers import api_router

app = FastAPI(description='Agente financeiro')


app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
