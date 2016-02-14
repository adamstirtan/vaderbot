import sys
import time
from slackclient import SlackClient
from database.databaseclient import DatabaseClient
from commands.urban_dictionary import urban_dictionary
from commands.scream import scream
from commands.scream_loud import scream_loud


class Vader:

    client = None
    database = None
    token = "xoxb-16470487171-NEqcYbtwqYrDWeXktwbWVUho"
    commands = {
        "!ud": urban_dictionary,
        "!scream": scream,
        "!SCREAM": scream_loud
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
                message = event["text"].split()
                channel = next(channel for channel in self.client.server.channels if channel.id == event["channel"])

                if len(message) == 0:
                    return

                for k, v in self.commands.items():
                    if message[0] == k:
                        v(channel, message[1:])

        except KeyError as e:
            print(str(e), file=sys.stderr)
            pass
