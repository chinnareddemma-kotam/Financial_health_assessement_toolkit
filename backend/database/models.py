from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from .database import Base

class SMESnapshot(Base):
    __tablename__ = "sme_snapshots"

    id = Column(Integer, primary_key=True, index=True)

    transaction_id = Column(String, nullable=True)
    revenue = Column(Float, nullable=True)
    profit_margin = Column(Float, nullable=True)
    cost_ratio = Column(Float, nullable=True)

    health_score = Column(Integer)
    health_status = Column(String)
    confidence = Column(Float)
    insight = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
