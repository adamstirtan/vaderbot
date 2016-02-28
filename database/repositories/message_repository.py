from database.repositories.repository import Repository


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
        return self.__get__(entity_id)

    def where(self, clause):
        return self.__where__(clause)

    def update(self, entity):
        return self.__update__(entity)

    def remove(self, entity):
        return self.__remove__(entity)
