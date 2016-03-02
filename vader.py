import time

from datetime import datetime
from slackclient import SlackClient
from database.database_client import DatabaseClient
from models import Message, Quote
from commands.add_point import AddPointCommand
from commands.add_quote import AddQuoteCommand
from commands.aol_say import AolSayCommand
from commands.convert import ConvertCommand
from commands.count import CountCommand
from commands.quote import QuoteCommand
from commands.scream import ScreamCommand
from commands.take_point import TakePointCommand
from commands.update import  UpdateCommand
from commands.urban_dictionary import UrbanDictionaryCommand
from commands.weather import WeatherCommand


class Vader:

    def __init__(self):
        database = DatabaseClient()

        self._client = SlackClient("xoxb-16470487171-NEqcYbtwqYrDWeXktwbWVUho")
        self._message_repository = database.repository(Message)
        self._commands = {
            "!addpoint": AddPointCommand(database.repository(Quote)),
            "!addquote": AddQuoteCommand(database.repository(Quote)),
            "!aolsay": AolSayCommand(),
            "!convert": ConvertCommand(),
            "!count": CountCommand(database.repository(Message), database.repository(Quote)),
            "!quote": QuoteCommand(database.repository(Quote)),
            "!scream": ScreamCommand(),
            "!SCREAM": ScreamCommand(loud=True),
            "!takepoint": TakePointCommand(database.repository(Quote)),
            "!ud": UrbanDictionaryCommand(),
            "!update": UpdateCommand(),
            "!weather": WeatherCommand()
        }

    def connect(self):
        self._client.rtm_connect()

        while True:
            for event in self._client.rtm_read():
                self.process_event(event)
            time.sleep(1)

    def process_event(self, event):
        try:
            if event["type"] == "message":
                message = event["text"]
                channel = next(channel for channel in self._client.server.channels if channel.id == event["channel"])
                user = next(user for user in self._client.server.users if user.id == event["user"])

                if message[0] != "!" and user.name != "vader":
                    self._message_repository.add(Message(user.name, message, datetime.now()))
                    return

                command = message.split()[0]

                if command == "!help":
                    channel.send_message("Available commands: {}"
                                         .format(", ".join(sorted(self._commands.keys(), key=lambda x: x.lower()))))
                    return

                for key, value in self._commands.items():
                    if command == key:
                        value.execute(channel, message.split()[1:])
                        break

        except (KeyError, StopIteration):
            pass
