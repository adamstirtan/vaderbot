import sqlite3
import zipfile

from database.repositories.message_repository import MessageRepository
from database.repositories.quote_repository import QuoteRepository
from database.repositories.user_repository import UserRepository


class DatabaseClient:

    database_file_name = "database/bot.db"
    migrations_file_name = "database/migrations/migrations.zip"

    def __init__(self):
        self.upgrade()

    @staticmethod
    def repository(cls):
        if cls.__name__ == "Message":
            return MessageRepository()
        elif cls.__name__ == "Quote":
            return QuoteRepository()
        elif cls.__name__ == "User":
            return UserRepository()

        return None

    def upgrade(self):
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

        zip_file = zipfile.ZipFile(self.migrations_file_name)

        for index, file_name in enumerate(zip_file.namelist()):
            with zip_file.open(file_name) as f:
                result.append((index + 1, f.read()))

        return result

    def __perform_upgrade__(self, statement):
        connection = None

        try:
            connection = sqlite3.connect(self.database_file_name)
            cursor = connection.cursor()

            cursor.execute(statement)

            connection.commit()
        finally:
            if connection:
                connection.close()

    def __get_schema_version__(self):
        connection = None

        try:
            connection = sqlite3.connect(self.database_file_name)
            cursor = connection.cursor()

            result = cursor.execute("PRAGMA user_version").fetchone()[0]
        finally:
            if connection:
                connection.close()

        return result

    def __set_schema_version__(self, version):
        connection = None

        try:
            connection = sqlite3.connect(self.database_file_name)
            cursor = connection.cursor()

            cursor.execute("PRAGMA user_version = {}".format(version))

            connection.commit()
        finally:
            if connection:
                connection.close()
