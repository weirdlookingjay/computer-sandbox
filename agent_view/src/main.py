from fastapi import FastAPI
from api import router as api_router
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Agent View")
app.include_router(api_router)
