import random

from commands.command import Command
import string

class ScreamCommand(Command):
    dont_scream = string.punctuation + string.whitespace
    max_length = 50
    default_word = "BWAUGH"

    def __init__(self, loud=False):
        Command.__init__(self)
        self.volume = 8 if not loud else 16

    def validate(self, parameters):
        if len(" ".join(parameters)) > self.max_length:
            return False
        return True

    def generate_output(self, parameters):
        if len(parameters) > 0:
            output = "   ".join([self._scream(word) for word in parameters])
        else:
            output = self._scream(self.default_word)

        return output.upper()

    def execute(self, channel, parameters):
        if self.validate(parameters):
            message = self.generate_output(parameters)
        else:
            message = "That's not a good idea."

        channel.send_message(message)

    def _scream(self, word):
        screamed = word[0]

        for c in word[1:]:
            if not c in self.dont_scream:
                screamed += c*random.randint(1,self.volume)
            else:
                screamed += c

        return screamed
