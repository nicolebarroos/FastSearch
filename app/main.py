from fastapi import FastAPI
from app.presentation.routes import router

app = FastAPI(title="FastSearch API", description="API de busca com Elasticsearch")

app.include_router(router)
