from sqlalchemy import Column, Integer, String

from .database import Base

class FactOrm(Base):
    __tablename__ = "facts"

    id = Column("id", Integer, primary_key=True)
    content = Column("content", String)



