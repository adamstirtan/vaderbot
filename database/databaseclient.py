import sqlite3


class DatabaseClient:

    db_file = "database/bot.db"

    def __init__(self):
        self.__initialize_tables__()

    def __initialize_tables__(self):
        db = self.open()

        cursor = db.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            user TEXT,
            message TEXT,
            message_time DATE)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY,
            quote TEXT,
            quote_time DATE,
            points INTEGER)''')

        db.commit()
        db.close()

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
            columns = ", ".join([description[0] for description in cursor.description]).replace("id, ", "")

            cursor.execute("INSERT INTO {} ({}) VALUES ({})"
                           .format(table, columns, ", ".join((columns.count(",") + 1) * "?")), entity)

            connection.commit()
        finally:
            if connection:
                connection.close()

        return cursor.lastrowid
