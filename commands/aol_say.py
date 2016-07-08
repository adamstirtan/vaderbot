import random

from commands.command import Command


class AolSayCommand(Command):

    def __init__(self):
        Command.__init__(self)

    def execute(self, channel, parameters):
        if len(parameters) > 0:
            channel.send_message("Usage: !aolsay")
            return

        channel.send_message(random.choice(list(open("commands/aolsay.txt", encoding="utf8"))))
