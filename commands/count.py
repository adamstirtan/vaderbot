from commands.command import Command


class CountCommand(Command):

    def __init__(self, message_repository, quote_repository):
        Command.__init__(self)

        self._message_repository = message_repository
        self._quote_repository = quote_repository

    def execute(self, channel, parameters):
        if len(parameters) == 0:
            channel.send_message("Usage: !count [messages or quotes]")
            return

        query = " ".join(parameters)

        if query == "messages":
            channel.send_message("There are {} messages in my database.".format(self._message_repository.count()))
        elif query == "quotes":
            channel.send_message("There are {} quotes in my database".format(self._quote_repository.count()))
        else:
            channel.send_message("Usage: !count [messages or quotes]")
