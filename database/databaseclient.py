import sqlite3

from os import listdir
from os.path import isfile, join


class DatabaseClient:

    db_file = "database/bot.db"

    def __init__(self):
        self.__upgrade_database__()

    def __upgrade_database__(self):
        migrations = self.__get_migrations__()
        schema_version = self.__get_schema_version__()

        for migration in migrations[schema_version:]:
            version = migration[0]
            statements = [s.strip() for s in migration[1].splitlines()]

            for statement in statements:
                self.__perform_upgrade__(statement)

            self.__set_schema_version__(version)

    @staticmethod
    def __get_migrations__():
        migrations_path = "database/migrations/"
        migrations =\
            [file for file in listdir(migrations_path) if isfile(join(migrations_path, file)) and file.endswith(".sql")]

        result = []
        for i in range(len(migrations)):
            result.append((i + 1, open(migrations_path + migrations[i], encoding="utf8").read()))

        return result

    def __perform_upgrade__(self, statement):
        connection = None

        try:
            connection = self.open()
            cursor = connection.cursor()

            cursor.execute(statement)

            connection.commit()
        finally:
            if connection:
                connection.close()

    def __get_schema_version__(self):
        connection = None

        try:
            connection = self.open()
            cursor = connection.cursor()

            result = cursor.execute("PRAGMA user_version").fetchone()[0]
        finally:
            if connection:
                connection.close()

        return result

    def __set_schema_version__(self, version):
        connection = None

        try:
            connection = self.open()
            cursor = connection.cursor()

            cursor.execute("PRAGMA user_version = {}".format(version))

            connection.commit()
        finally:
            if connection:
                connection.close()

    def open(self):
        return sqlite3.connect(self.db_file)

    def count(self, table):
        connection = None

        try:
            connection = self.open()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            result = cursor.execute("SELECT COUNT(id) FROM {}".format(table)).fetchone()
        finally:
            if connection:
                connection.close()

        return int(result[0])

    def insert(self, table, entity):
        connection = None

        try:
            connection = self.open()
            cursor = connection.execute("SELECT * FROM {}".format(table))
            columns = ", ".join(description[0] for description in cursor.description[1:])

            cursor.execute("INSERT INTO {} ({}) VALUES ({})"
                           .format(table, columns, ", ".join((columns.count(",") + 1) * "?")), entity)

            connection.commit()
        finally:
            if connection:
                connection.close()

        return cursor.lastrowid
