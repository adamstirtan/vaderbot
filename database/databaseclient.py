import sqlite3
from datetime import datetime


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
        return sqlite3.connect(self.db_file, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

    def add_message(self, user, message):
        db = self.open()

        cursor = db.cursor()
        cursor.execute('''INSERT INTO messages (user, message, message_time) VALUES (?, ?, ?)''',
                       (user, message, datetime.now()))

        db.commit()
        db.close()

        return cursor.lastrowid

    def add_quote(self, quote):
        db = self.open()

        cursor = db.cursor()
        cursor.execute('''INSERT INTO quotes (quote, quote_time, points) VALUES (?, ?, ?)''',
                       (quote, datetime.now(), 0))

        db.commit()
        db.close()

        return cursor.lastrowid
