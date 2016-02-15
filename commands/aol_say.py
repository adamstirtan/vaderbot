from random import choice


def aol_say(database, channel, params):
    if len(params) > 0:
        channel.send_message("Usage: !aolsay")
        return

    channel.send_message(choice(list(open("commands/aolsay.txt"))))
