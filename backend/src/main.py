from fastapi import FastAPI

from backend.api import router as api_router

app = FastAPI(title="Computer Management Backend")

app.include_router(api_router)
