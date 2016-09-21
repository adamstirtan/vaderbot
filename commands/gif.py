import requests
import json
import os
import random

try:
    from commands.command import Command
except ImportError:
    from command import Command


class GifCommand(Command):

    def __init__(self):
        Command.__init__(self)
        self._request_uri = "http://api.giphy.com/v1/gifs/search?q={}&api_key={}"
        self._api_key = "dc6zaTOxFJmzC"

    def validate(self, parameters):
        if len(parameters) == 0:
            return False
        return True

    def create_output(self, parameters):
        pass

    def execute(self, channel, parameters):
        if len(parameters) == 0:
            return

        query = "+".join(parameters)

        try:
            response = requests.get(self._request_uri.format(query, self._api_key))
            if response.status_code == 200:
                data = json.loads(response.text)
                choices = []
                for gif in data["data"]:
                    if gif["type"] == "gif":
                        choices.append(gif["url"])
                        if len(choices) == 10:
                            break
            else:
                data = "I don't know!"
        except Exception as e:
            data = "I don't know!"

        channel.send_message(random.choice(choices))

if __name__ == "__main__":
    from fakechannel import FakeChannel
    channel = FakeChannel()
    g = GifCommand()
    g.execute(channel, ["cat"])
