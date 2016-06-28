from commands.command import Command


class FreqCommand(Command):

    def __init__(self, message_repository, message = None):
        Command.__init__(self)

        self._message_repository = message_repository
        self.message = message

    def execute(self, channel, parameters):
        if len(parameters) != 1 and self.message is None:
            channel.send_message("Usage: !freq [word]")
            return

        word = parameters[0] if not self.message else self.message
        freq = self._message_repository.freq(word)
        channel.send_message("The word {} has been logged {} time{}.".format(word, freq, "s" if not freq == 1 else ""))
