from database.repositories.repository import Repository
from models import Quote


class QuoteRepository(Repository):

    def __init__(self):
        Repository.__init__(self)

    def table_name(self):
        return "quotes"

    def add(self, entity):
        return self.__add__(entity)

    def all(self):
        return self.__all__()

    def get(self, entity_id):
        entity = self.__get__(entity_id)
        return Quote(entity[1], entity[2], entity[0]) if entity else None

    def where(self, clause):
        return self.__where__(clause)

    def update(self, entity):
        with self.open() as connection:
            cursor = connection.cursor()
            query = "UPDATE quotes SET quote = ?, points = ? WHERE id=?"

            cursor.execute(query, (entity.quote, entity.points, entity.entity_id))
            return entity

    def remove(self, entity):
        return self.__remove__(entity)

    def random(self):
        with self.open() as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1"

            entity = cursor.execute(query).fetchone()
            return Quote(entity[1], entity[2], entity[0]) if entity else None

    def search(self, clause):
        with self.open() as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM quotes WHERE {} ORDER BY RANDOM() LIMIT 1".format(clause)

            entity = cursor.execute(query).fetchone()
            return Quote(entity[1], entity[2], entity[0]) if entity else None
