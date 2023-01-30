import connect
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String, Column
from sqlalchemy import insert, select
from sqlalchemy.orm import Session

db = connect.connectDb()

Base = declarative_base()


class Dictionary(Base):
    __tablename__ = 'dictionaries'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    session = Session(db)
    db = db

    def getAll(self):
        stmt = select(Dictionary)
        return self.session.scalars(stmt)

    def getOneById(self, id):
        stmt = select(Dictionary).where(Dictionary.id == id)
        return self.session.scalar(stmt)

    def AddDictionary(self, data):
        stmt = insert(Dictionary).values(
            title=data['title']
        )
        self.db.connect().execute(stmt)
        return 1
