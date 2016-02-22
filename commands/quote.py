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
    result = cursor.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1").fetchone()

    db.close()

    if result:
        channel.send_message("#{} - {} points".format(result[0], result[2]))
        channel.send_message(result[1])


def __id_quote__(database, channel, quote_id):
    entity = database.get("quotes", quote_id)

    if quote:
        channel.send_message("#{} - {} points".format(entity[0], entity[2]))
        channel.send_message(entity[1])
