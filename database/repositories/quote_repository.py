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

        if entity:
            return Quote(entity[1], entity[2], entity[0])
        return None

    def where(self, clause):
        return self.__where__(clause)

    def update(self, entity):
        return self.__update__(entity)

    def remove(self, entity):
        return self.__remove__(entity)

    def random(self):
        connection = None

        try:
            connection = self.open()
            cursor = connection.cursor()

            entity = cursor.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1").fetchone()
        finally:
            if connection:
                connection.close()

        return Quote(entity[1], entity[2], entity[0]) if entity else None
