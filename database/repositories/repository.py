import sqlite3

from abc import ABCMeta, abstractclassmethod


class Repository:
    __metaclass__ = ABCMeta

    @staticmethod
    def open():
        return sqlite3.connect("database/bot.db")

    @abstractclassmethod
    def table_name(self):
        pass

    def count(self):
        connection = None

        try:
            connection = self.open()
            cursor = connection.cursor()
            query = "SELECT COUNT(id) FROM {}".format(self.table_name())

            result = cursor.execute(query).fetchone()
        finally:
            if connection:
                connection.close()

        return int(result[0])

    def __add__(self, entity):
        connection = None

        try:
            connection = self.open()
            cursor = connection.execute("SELECT * FROM {}".format(entity.table_name()))
            columns = ", ".join(description[0] for description in cursor.description[1:])
            query = "INSERT INTO {} ({}) VALUES ({})".format(
                entity.table_name(), columns, ", ".join((columns.count(",") + 1) * "?"))

            cursor.execute(query, entity.to_tuple())

            connection.commit()
        finally:
            if connection:
                connection.close()

        return cursor.lastrowid

    def __all__(self):
        connection = None

        try:
            connection = self.open()
            cursor = connection.cursor()
            query = "SELECT * FROM {}".format(self.table_name())

            entities = cursor.execute(query).fetchall()
        finally:
            if connection:
                connection.close()

        return entities

    def __get__(self, entity_id):
        connection = None

        try:
            connection = self.open()
            cursor = connection.cursor()
            query = "SELECT * FROM {} where id=?".format(self.table_name())

            entity = cursor.execute(query, (entity_id,)).fetchone()
        finally:
            if connection:
                connection.close()

        return entity

    def __where__(self, clause):
        connection = None

        try:
            connection = self.open()
            cursor = connection.cursor()
            query = "SELECT * FROM [] WHERE {}".format(self.table_name(), clause)

            result = cursor.execute(query).fetchall()
        finally:
            if connection:
                connection.close()

        return result

    @abstractclassmethod
    def update(self, entity):
        pass

    def __remove__(self, entity):
        connection = None

        try:
            connection = self.open()
            query = "DELETE FROM {} WHERE id-?".format(self.table_name())

            connection.execute(query, (entity.entity_id,))
        finally:
            if connection:
                connection.close()
