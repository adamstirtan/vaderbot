def count(database, channel, params):
    if len(params) == 0:
        channel.send_message("Usage: !count [messages or quotes]")
        return

    query = " ".join(params)

    if query == "messages" or query == "quotes":
        channel.send_message("There are {} {} in my database.".format(database.count(query), query))
    else:
        channel.send_message("Usage: !count [messages or quotes]")
