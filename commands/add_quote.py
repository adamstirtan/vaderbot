from datetime import datetime


def add_quote(database, channel, params):
    if len(params) == 0:
        channel.send_message("Usage: !addquote [message]")
        return

    message = " ".join(params)

    db = database.open()

    cursor = db.cursor()
    cursor.execute(
        '''INSERT INTO quotes (quote, quote_time, points) VALUES (?, ?, ?)''',
        (message, datetime.now(), 0))

    db.commit()
    db.close()

    channel.send_message("Bleep bloop! Quote number {} added.".format(cursor.lastrowid))
