import time

from datetime import datetime
from slackclient import SlackClient
from database.databaseclient import DatabaseClient
from commands.add_quote import add_quote
from commands.aol_say import aol_say
from commands.count import count
from commands.quote import quote
from commands.scream import scream
from commands.scream_loud import scream_loud
from commands.urban_dictionary import urban_dictionary


class Vader:

    client = None
    database = None
    token = "xoxb-16470487171-NEqcYbtwqYrDWeXktwbWVUho"
    commands = {
        "!addquote": add_quote,
        "!aolsay": aol_say,
        "!count": count,
        "!quote": quote,
        "!scream": scream,
        "!SCREAM": scream_loud,
        "!ud": urban_dictionary
    }

    def __init__(self):
        self.client = SlackClient(self.token)
        self.database = DatabaseClient()

    def connect(self):
        self.client.rtm_connect()

        while True:
            events = self.client.rtm_read()

            for event in events:
                self.process_event(event)

            time.sleep(1)

    def process_event(self, event):
        try:
            if event["type"] == "message":
                message = event["text"]
                channel = next(channel for channel in self.client.server.channels if channel.id == event["channel"])
                user = next(user for user in self.client.server.users if user.id == event["user"])

                if message[0] != "!" and user.name != "vader":
                    self.database.insert("messages", (user, message, datetime.now()))
                    return

                command, *params = message.split()

                if command in self.commands:
                    self.commands[command](self.database, channel, params)

        except KeyError:
            pass
