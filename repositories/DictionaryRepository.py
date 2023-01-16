from sqlalchemy import insert, select
from sqlalchemy.orm import Session


class DictionaryRepository:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.session = Session(self.dictionary.db)

    def getAll(self):
        stmt = select(self.dictionary)
        return self.session.scalars(stmt)

    def getOneById(self, id):
        stmt = select(self.dictionary).where(self.dictionary.id == id)
        return self.session.scalar(stmt)


    def AddDictionary(self, data):
        stmt = insert(self.dictionary).values(
            title = data['title']
        )
        self.dictionary.db.connect().execute(stmt)
        return 1