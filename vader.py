#!/usr/bin/env python3

import time
import commands
from slackclient import SlackClient


class Vader:

    client = None
    token = "xoxb-16470487171-NEqcYbtwqYrDWeXktwbWVUho"
    channel = "general"
    commands = {"!ud": commands.urban_dictionary}

    def __init__(self):
        self.client = SlackClient(self.token)

    def connect(self):
        self.client.rtm_connect()
        while True:
            events = self.client.rtm_read()
            for event in events:
                self.process_event(event)
            time.sleep(1)

    def process_event(self, event):
        print("Event: {}".format(event))
        try:
            if event["type"] == "message":
                message_text = event["text"]
                split = message_text.split()
                if len(split) == 0:
                    return
                for k, v in self.commands.items():
                    if split[0] == k:
                        v(self.client, self.channel, split[1:])
        except KeyError:
            pass


Vader().connect()
