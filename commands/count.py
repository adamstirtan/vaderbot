def count(database, channel, params):
    if len(params) == 0:
        channel.send_message("Usage: !count [messages or quotes]")
        return

    query = " ".join(params)

    if query == "messages":
        result = __count_messages__(database)
        channel.send_message("There are {} messages in my database.".format(result))
    elif query == "quotes":
        result = __count_quotes__(database)
        channel.send_message("There are {} quotes in my database.".format(result))


def __count_messages__(database):
    db = database.open()

    cursor = db.cursor()
    result = cursor.execute('''SELECT count(id) FROM messages''').fetchone()

    db.close()

    return int(result[0])

def __count_quotes__(database):
    db = database.open()

    cursor = db.cursor()
    result = cursor.execute('''SELECT count(id) FROM quotes''').fetchone()

    db.close()

    return int(result[0])
