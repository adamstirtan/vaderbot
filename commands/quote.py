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
            self.__search_quote__(channel, parameters)

    def __random_quote__(self, channel):
        quote = self._quote_repository.random()

        if quote:
            channel.send_message("#{} - {} points\n```{}```".format(quote.entity_id, quote.points, quote.quote))

    def __id_quote__(self, channel, quote_id):
        quote = self._quote_repository.get(quote_id)

        if quote:
            channel.send_message("#{} - {} points\n```{}```".format(quote.entity_id, quote.points, quote.quote))
        else:
            channel.send_message("There is no quote with that number.")

    def __search_quote__(self, channel, query):
        quote = None
        query = " ".join(query)

        if query[0] == "*" and query[-1] != "*":
            quote = self._quote_repository.search("quote LIKE \'%{}\'".format(query[1:]))
        elif query[0] != "*" and query[-1] == "*":
            quote = self._quote_repository.search("quote LIKE \'{}%\'".format(query[:-1]))
        elif query[0] == "*" and query[-1] == "*":
            quote = self._quote_repository.search("quote LIKE \'%{}%\'".format(query[1:-1]))

        if quote:
            channel.send_message("#{} - {} points\n```{}```".format(quote.entity_id, quote.points, quote.quote))
        else:
            channel.send_message("Couldn't find anything that matched {}".format(query))
