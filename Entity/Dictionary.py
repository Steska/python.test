import connect
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String, Column

db = connect.connectDb()

Base = declarative_base()

class Dictionary(Base):
    __tablename__ = 'dictionaries'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)

    db = db
