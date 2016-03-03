import sqlite3

from abc import ABCMeta, abstractmethod


class Repository:
    __metaclass__ = ABCMeta

    @staticmethod
    def open():
        return sqlite3.connect("database/bot.db")

    @abstractmethod
    def table_name(self):
        pass

    def count(self):
        with self.open() as connection:
            cursor = connection.cursor()
            query = "SELECT COUNT(id) FROM {}".format(self.table_name())

            return int(cursor.execute(query).fetchone()[0])

    def __add__(self, entity):
        with self.open() as connection:
            cursor = connection.execute("SELECT * FROM {}".format(entity.table_name()))
            columns = ", ".join(description[0] for description in cursor.description[1:])
            query = "INSERT INTO {} ({}) VALUES ({})".format(
                entity.table_name(), columns, ", ".join((columns.count(",") + 1) * "?"))

            cursor.execute(query, entity.to_tuple())
            connection.commit()

            return cursor.lastrowid

    def __all__(self):
        with self.open() as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM {}".format(self.table_name())

            return cursor.execute(query).fetchall()

    def __get__(self, entity_id):
        with self.open() as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM {} where id=?".format(self.table_name())

            return cursor.execute(query, (entity_id,)).fetchone()

    def __where__(self, clause):
        with self.open() as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM [] WHERE {}".format(self.table_name(), clause)

            return cursor.execute(query).fetchall()

    @abstractmethod
    def update(self, entity):
        pass

    def __remove__(self, entity):
        with self.open() as connection:
            query = "DELETE FROM {} WHERE id-?".format(self.table_name())

            connection.execute(query, (entity.entity_id,))
