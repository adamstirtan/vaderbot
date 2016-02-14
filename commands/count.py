def count(database, channel, params):
    if len(params) == 0:
        print("Usage: !count (messages, quotes)")
        return

    query = " ".join(params)

    if query == "messages":
        result = __count_messages__(database)
        channel.send_message("There are {} messages in my database".format(result))


def __count_messages__(database):
    db = database.open()
    cursor = db.cursor()

    result = cursor.execute('''SELECT count(id) FROM messages''').fetchone()

    return int(result[0])
