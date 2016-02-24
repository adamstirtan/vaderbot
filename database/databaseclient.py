import sqlite3
import zipfile


class DatabaseClient:

    db_file = "database/bot.db"
    migrations_file = "database/migrations/migrations.zip"

    def __init__(self):
        self.__upgrade_database__()

    def __upgrade_database__(self):
        migrations = self.__get_migrations__()
        schema_version = self.__get_schema_version__()

        for migration in migrations[schema_version:]:
            version = migration[0]
            statements = [s.strip().decode("utf8") for s in migration[1].splitlines()]
            for statement in statements:
                self.__perform_upgrade__(statement)

            self.__set_schema_version__(version)

    def __get_migrations__(self):
        result = []

        zip_file = zipfile.ZipFile(self.migrations_file)

        for index, file_name in enumerate(zip_file.namelist()):
            with zip_file.open(file_name) as f:
                result.append((index + 1, f.read()))

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
            cursor = connection.cursor()

            result = cursor.execute("SELECT COUNT(id) FROM {}".format(table)).fetchone()
        finally:
            if connection:
                connection.close()

        return int(result[0])

    def all(self, table):
        connection = None

        try:
            connection = self.open()
            cursor = connection.cursor()

            result = cursor.execute("SELECT * FROM {}".format(table)).fetchall()
        finally:
            if connection:
                connection.close()

        return result

    def get(self, table, entity_id):
        connection = None

        try:
            connection = self.open()
            cursor = connection.cursor()

            result = cursor.execute("SELECT * FROM {} WHERE id=?".format(table), (entity_id,)).fetchone()
        finally:
            if connection:
                connection.close()

        return result

    def where(self, table, clause):
        connection = None

        try:
            connection = self.open()
            cursor = connection.cursor()

            result = cursor.execute("SELECT * FROM {} WHERE {}".format(table, clause)).fetchall()
        finally:
            if connection:
                connection.close()

        return result

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

    def update(self, table, entity_id, updated_entity):
        connection = None

        try:
            connection = self.open()
            cursor = connection.execute("SELECT * FROM {}".format(table))

            columns = []
            for k, v in updated_entity.items():
                columns.append(str(k) + " = " + str(v))

            cursor.execute("UPDATE {} SET {} WHERE id=?".format(table, ", ".join(columns)), (entity_id,))

            connection.commit()
        finally:
            if connection:
                connection.close()
