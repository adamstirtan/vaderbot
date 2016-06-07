from commands.command import Command


class FreqCommand(Command):

    def __init__(self, message_repository):
        Command.__init__(self)

        self._message_repository = message_repository

    def execute(self, channel, parameters):
        if len(parameters) != 1:
            channel.send_message("Usage: !freq [word]")
            return

        word = parameters[0]
        freq = self._message_repository.freq(word)
        channel.send_message("The word {} has been logged {} time{}.".format(word, freq, "s" if not freq == 1 else ""))
