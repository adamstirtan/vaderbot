import sqlite3


class DatabaseClient:

    @staticmethod
    def open():
        return sqlite3.connect("database/bot.db")

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
