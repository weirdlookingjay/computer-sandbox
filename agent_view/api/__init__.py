from fastapi import APIRouter
from src.status import router as status_router

router = APIRouter()
router.include_router(status_router)

@router.get("/ping")
def ping():
    return {"status": "agent ok"}
