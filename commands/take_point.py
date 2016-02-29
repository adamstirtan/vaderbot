from commands.command import Command


class TakePointCommand(Command):

    def __init__(self, quote_repository):
        Command.__init__(self)

        self._quote_repository = quote_repository

    def execute(self, channel, parameters):
        if len(parameters) != 1:
            channel.send_message("Usage: !takepoint [quote number]")
            return

        quote = self._quote_repository.get(parameters[0])

        if quote:
            quote.points -= 1
            self._quote_repository.update(quote)
            channel.send_message("Bleep bloop! Quote number {} updated.".format(quote.entity_id))
        else:
            channel.send_message("There is no quote with that number.")
