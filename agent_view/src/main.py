from fastapi import FastAPI

from agent_view.api import router as api_router

app = FastAPI(title="Agent View")

app.include_router(api_router)
