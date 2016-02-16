def add_quote(database, channel, params):
    if len(params) == 0:
        channel.send_message("Usage: !addquote [message]")
        return

    message = " ".join(params)

    result = database.insert("quotes", (message, 0))

    channel.send_message("Bleep bloop! Quote number {} added.".format(result))
