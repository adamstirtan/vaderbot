import time
import os

from datetime import datetime
from slackclient import SlackClient

from database.database_client import DatabaseClient
from models import Message, Quote, TriviaQuestion, User
from commands.add_point import AddPointCommand
from commands.add_quote import AddQuoteCommand
from commands.aol_say import AolSayCommand
from commands.convert import ConvertCommand
from commands.count import CountCommand
from commands.eight_ball import EightBallCommand
from commands.freq import FreqCommand
from commands.quote import QuoteCommand
from commands.scream import ScreamCommand
from commands.take_point import TakePointCommand
from commands.trivia import TriviaCommand
from commands.update import UpdateCommand
from commands.urban_dictionary import UrbanDictionaryCommand
from commands.weather import WeatherCommand
from commands.wordfreq import WordFreqCommand


# noinspection PyBroadException
class Vader:

    def __init__(self):
        self._api_key = os.getenv("SLACK_API_KEY")
        self._client = SlackClient(self._api_key)
        database = DatabaseClient()

        self._message_repository = database.repository(Message)
        self._commands = {
            "!8ball": EightBallCommand(),
            "!addpoint": AddPointCommand(database.repository(Quote)),
            "!addquote": AddQuoteCommand(database.repository(Quote)),
            "!aolsay": AolSayCommand(),
            "!convert": ConvertCommand(),
            "!count": CountCommand(database.repository(Message), database.repository(Quote)),
            "!freq": FreqCommand(database.repository(Message)),
            "!kenken": FreqCommand(database.repository(Message), "kenken"),
            "!quote": QuoteCommand(database.repository(Quote)),
            "!scream": ScreamCommand(),
            "!SCREAM": ScreamCommand(loud=True),
            "!takepoint": TakePointCommand(database.repository(Quote)),
            "!trivia": TriviaCommand(database.repository(TriviaQuestion), database.repository(User)),
            "!ud": UrbanDictionaryCommand(),
            "!update": UpdateCommand(),
            "!weather": WeatherCommand(),
            "!wordcloud": WordFreqCommand(self._client, self._api_key),
        }

    def start(self):
        self.connect()

        while True:
            try:
                for event in self._client.rtm_read():
                    self.process_event(event)
                    print(event)
                time.sleep(1)
            except Exception as e:
                print("Something went wrong...reconnecting")
                print(e)
                self.connect()

    def _handle_event(self):
        pass

    def connect(self):
        if self._client:
            self._client = SlackClient(self._api_key)

        self._client.rtm_connect()

    def process_event(self, event):
        try:
            if event["type"] == "message":
                message = event["text"]
                channel = next(channel for channel in self._client.server.channels if channel.id == event["channel"])
                user = next(user for user in self._client.server.users if user.id == event["user"])

                if message[0] != "!" and user.name != "spaderbot":
                    self._message_repository.add(Message(user.name, message, datetime.now()))
                    return

                command = message.split()[0]

                if command == "!help":
                    channel.send_message("Available commands: {}"
                                         .format(", ".join(sorted(self._commands.keys(), key=lambda x: x.lower()))))
                    return
                message = self._check_users(message)
                if command == "!update":
                    channel.send_message("I'm sorry, {}. I'm afraid I can't do that.".format(user.name))
                    if not user.name == "madl":
                        return
                for key, value in self._commands.items():
                    if command == key:
                        value.execute(channel, message.split()[1:])
                        break
        except Exception as e:
            print(e)

    def _check_users(self, parameters):
        new_parameters = []
        for param in parameters.split():
            if param.startswith("<"):
                maybe_user = param[2:-1]
                for user in self._client.server.users:
                    if user.id == maybe_user:
                        new_parameters.append("@"+user.name)
                        break
            else:
                new_parameters.append(param)
        return " ".join(new_parameters)

