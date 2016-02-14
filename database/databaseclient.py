import sqlite3


class DatabaseClient:

    db_file = "database/bot.db"

    def __init__(self):
        self.initialize_tables()

    def initialize_tables(self):
        db = sqlite3.connect(self.db_file)

        cursor = db.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            user TEXT,
            message TEXT,
            message_time DATE)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY,
            user TEXT,
            quote TEXT,
            quote_time DATE)''')

        db.commit()
        db.close()

    def add_message(self, message, user):
        pass
