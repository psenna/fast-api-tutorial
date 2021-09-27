from fastapi import FastAPI

from rotas import router

app = FastAPI()

app.include_router(router, prefix="")
