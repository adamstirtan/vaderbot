from datetime import datetime


def add_quote(database, channel, params):
    if len(params) == 0:
        channel.send_message("Usage: !addquote [message]")
        return

    message = " ".join(params)

    result = database.insert("quotes", (message, datetime.now(), 0))

    channel.send_message("Bleep bloop! Quote number {} added.".format(result))
