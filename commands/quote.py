from commands.command import Command


class QuoteCommand(Command):

    def __init__(self, quote_repository):
        Command.__init__(self)

        self._quote_repository = quote_repository

    def execute(self, channel, parameters):
        if len(parameters) == 0:
            self.__random_quote__(channel)
        elif len(parameters) == 1 and parameters[0].isdigit():
            self.__id_quote__(channel, parameters[0])
        else:
            channel.send_message("Usage: !quote [optional: query]")

    def __random_quote__(self, channel):
        quote = self._quote_repository.random()

        if quote:
            channel.send_message("#{} - {} points\n{}".format(quote.entity_id, quote.points, quote.quote))

    def __id_quote__(self, channel, quote_id):
        quote = self._quote_repository.get(quote_id)

        if quote:
            channel.send_message("#{} - {} points\n{}".format(quote.entity_id, quote.points, quote.quote))
