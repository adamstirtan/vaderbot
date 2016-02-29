import random

from commands.command import Command


class ScreamCommand(Command):

    def __init__(self):
        Command.__init__(self)

    def execute(self, channel, parameters):
        word = " ".join(parameters)

        if len(word) > 50:
            channel.send_message("That's not a good idea.")
            return
        elif word == "":
            word = "BWAUGH"

        word = word.upper()

        channel.send_message((lambda w: w[0] + "".join(c * random.randint(1, 8) for c in word[1:]))(word))
