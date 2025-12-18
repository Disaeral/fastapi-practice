from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import TIMESTAMP, func
from datetime import datetime

class Timestamp():
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())