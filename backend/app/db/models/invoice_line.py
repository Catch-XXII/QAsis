from sqlalchemy import Column, ForeignKey, Integer, Numeric

from app.db.database import Base


class InvoiceLine(Base):
    __tablename__ = "invoice_line"

    invoice_line_id = Column("invoice_line_id", Integer, primary_key=True)
    invoice_id = Column("invoice_id", Integer, ForeignKey("invoice.invoice_id"), nullable=False)
    track_id = Column("track_id", Integer, ForeignKey("track.track_id"), nullable=False)
    unit_price = Column("unit_price", Numeric, nullable=False)
    quantity = Column("quantity", Integer, nullable=False)
