#!/usr/bin/env python3

import time
from slackclient import SlackClient


class Vader:

    client = None
    token = "xoxb-16470487171-NEqcYbtwqYrDWeXktwbWVUho"

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
        try:
            if event["type"] == "message":
                print(event["text"])
        except KeyError:
            pass


Vader().connect()
