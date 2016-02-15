def quote(database, channel, params):
    if len(params) == 0:
        __random_quote__(database, channel)
    elif len(params) == 1 and params[0].isdigit():
        __id_quote__(database, channel, params[0])
    else:
        channel.send_message("Usage: !quote [optional: query]")


def __random_quote__(database, channel):
    db = database.open()

    cursor = db.cursor()
    result = cursor.execute(
        '''SELECT id, quote FROM quotes ORDER BY RANDOM() LIMIT 1''').fetchone()

    db.close()

    if result:
        channel.send_message("({}) {}".format(result[0], result[1]))
    else:
        channel.send_message("There are no quotes yet.")


def __id_quote__(database, channel, quote_id):
    db = database.open()

    cursor = db.cursor()
    result = cursor.execute(
        '''SELECT id, quote FROM quotes WHERE id=?''', (quote_id,)).fetchone()

    db.close()

    if result:
        channel.send_message("({}) {}".format(result[0], result[1]))
    else:
        channel.send_message("There is no quote with that number.")
