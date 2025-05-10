from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.app.db.database import Base
from datetime import datetime


class SearchAnalytics(Base):
    __tablename__ = "SearchAnalytics"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(String, nullable=False)

    ip = Column(String(64), nullable=True)
    country = Column(String(64), nullable=True)
    city = Column(String(64), nullable=True)

    browser = Column(String(64), nullable=True)
    os = Column(String(64), nullable=True)
    device = Column(String(64), nullable=True)
    user_agent = Column(String(256), nullable=True)

    timestamp = Column(DateTime(timezone=True), default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("Users.id"), nullable=True)
    user = relationship("User", backref="searches")
