def add_quote(database, channel, params):
    if len(params) == 0:
        channel.send_message("Usage: !addquote [message]")
        return

    message = " ".join(params)

    quote_id = database.add_quote(message)

    channel.send_message("Bleep bloop! Quote number {} added.".format(quote_id))
