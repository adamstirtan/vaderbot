from database.repositories.repository import Repository
from models import Message


class MessageRepository(Repository):

    def __init__(self):
        Repository.__init__(self)

    def table_name(self):
        return "messages"

    def add(self, entity):
        return self.__add__(entity)

    def all(self):
        return self.__all__()

    def get(self, entity_id):
        entity = self.__get__(entity_id)
        return Message(entity[1], entity[2], entity[3], entity[0])

    def where(self, clause):
        return self.__where__(clause)

    def update(self, entity):
        with self.open() as connection:
            cursor = connection.cursor()
            query = "UPDATE users SET user = {}, message = {}, message_time = {} WHERE id=?".format(
                entity.user, entity.message, entity.message_time)

            cursor.execute(query, (entity.entity_id,))
            return entity

    def remove(self, entity):
        return self.__remove__(entity)
