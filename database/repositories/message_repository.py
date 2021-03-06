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

    def freq(self, word):
        word = word.lower()
        query = "SELECT message FROM messages WHERE message LIKE \"% {} %\" OR message LIKE \"%{} %\" OR message LIKE \"% {}%\"".format(word, word, word)
        with self.open() as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            n = cursor.fetchall()
        return sum(s[0].lower().count(word) for s in n)

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
