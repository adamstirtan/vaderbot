from commands.command import Command
from models import Quote


class AddQuoteCommand(Command):

    def __init__(self, quote_repository):
        Command.__init__(self)

        self._quote_repository = quote_repository

    def execute(self, channel, parameters):
        if len(parameters) == 0:
            channel.send_message("Usage: !addquote [message]")
            return

        result = self._quote_repository.add(Quote(" ".join(parameters), 0))

        channel.send_message("Bleep bloop! Quote number {} added.".format(result))
