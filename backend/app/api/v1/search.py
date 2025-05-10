# app/api/v1/endpoints/search_schema.py

from fastapi import APIRouter, Request, Depends
from backend.app.db.schemas.search_schema import SearchRequestSchema
from typing import Optional
from datetime import datetime, timezone

router = APIRouter()


@router.post("/search")
async def search(
    request_data: SearchRequestSchema,
    request: Request,
    user: Optional[dict] = Depends(get_current_user_optional),
):
    client_ip = request.client.host
    user_agent = request.headers.get("user-agent", "unknown")
    now_utc = datetime.now(timezone.utc)

    log_data = {
        "query": request_data.query,
        "ip": client_ip,
        "user_agent": user_agent,
        "datetime_utc": now_utc.isoformat(),
        "user": user or "anonymous",
    }

    # (Burada DB'ye yazacağız — bir sonraki adım)
    print(log_data)  # şimdilik loglayalım

    return {"message": "Search logged", "data": log_data}
