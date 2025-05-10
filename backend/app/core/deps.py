from fastapi import Depends, Request
from jose import JWTError, jwt
from typing import Optional
from backend.app.db.models.user import User
from backend.app.db.session import get_db
from sqlalchemy.orm import Session
from backend.app.core.config import settings


def get_current_user_optional(
    request: Request, db: Session = Depends(get_db)
) -> Optional[User]:
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return None

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        user_id = payload.get("sub")
        if user_id is None:
            return None
        user = db.query(User).filter(User.id == int(user_id)).first()
        return user
    except JWTError:
        return None
