from subprocess import call


def update(database, channel, params):
    if len(params) != 0:
        channel.send_message("Usage: !update")
        return

    call("systemctl restart vaderbot")
