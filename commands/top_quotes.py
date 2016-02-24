def top_quotes(database, channel, params):
    if len(params) != 0:
        channel.send_message("Usage: !topquotes")
        return

    quotes = database.where("quotes", "points > 0")
