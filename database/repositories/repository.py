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

            result = cursor.execute("SELECT COUNT(id) FROM {}".format(self.table_name())).fetchone()
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

            cursor.execute("INSERT INTO {} ({}) VALUES ({})".format(entity.table_name(), columns,
                                                                    ", ".join((columns.count(",") + 1) * "?")),
                           entity.to_tuple())

            connection.commit()
        finally:
            if connection:
                connection.close()

    def __all__(self):
        connection = None

        try:
            connection = self.open()
            cursor = connection.cursor()

            entities = cursor.execute("SELECT * FROM {}".format(self.table_name())).fetchall()
        finally:
            if connection:
                connection.close()

        return entities

    def __get__(self, entity_id):
        connection = None

        try:
            connection = self.open()
            cursor = connection.cursor()

            entity = cursor.execute("SELECT * FROM {} where id=?".format(self.table_name()), (entity_id,)).fetchone()
        finally:
            if connection:
                connection.close()

        return entity

    def __where__(self, clause):
        connection = None

        try:
            connection = self.open()
            cursor = connection.cursor()

            result = cursor.execute("SELECT * FROM [] WHERE {}".format(self.table_name(), clause)).fetchall()
        finally:
            if connection:
                connection.close()

        return result

    def __update__(self, entity):
        connection = None

        try:
            connection = self.open()
            cursor = connection.execute("SELECT * FROM {}".format(entity.table_name()))

            columns = []
            for k, v in entity.items():
                columns.append(str(k) + " = " + str(v))

            cursor.execute("UPDATE {} SET {} WHERE id=?"
                           .format(entity.table_name(), ", ".join(columns)), (entity.entity_id,))

            connection.commit()
        finally:
            if connection:
                connection.close()

    def __remove__(self, entity):
        connection = None

        try:
            connection = self.open()
            connection.execute("DELETE FROM {} WHERE id-?".format(self.table_name()), (entity.entity_id,))
        finally:
            if connection:
                connection.close()
