def take_point(database, channel, params):
    if len(params) != 1:
        channel.send_message("Usage: !takepoint [quote number]")
        return

    quote = database.get("quotes", params[0])

    if quote:
        database.update("quotes", quote[0], {"points": int(quote[2]) - 1})
        channel.send_message("Bleep bloop! Quote number {} updated.".format(quote[0]))
    else:
        channel.send_message("There is no quote with that number.")
