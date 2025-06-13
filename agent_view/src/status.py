import psutil
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
import os

router = APIRouter()

@router.get("/status")
def get_status(request: Request):
    import os
    AGENT_TOKEN = os.getenv("AGENT_TOKEN")
    print("Loaded AGENT_TOKEN:", AGENT_TOKEN)
    auth = request.headers.get("authorization")
    if not auth or auth.replace("Bearer ", "") != AGENT_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    return JSONResponse({
        "cpu": cpu,
        "memory": mem,
        "disk": disk,
        "status": "ok"
    })
