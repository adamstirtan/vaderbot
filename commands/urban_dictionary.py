import requests
import json

from commands.command import Command


class UrbanDictionaryCommand(Command):

    def __init__(self):
        Command.__init__(self)

        self._request_uri = "http://api.urbandictionary.com/v0/define?term={}"

    def execute(self, channel, parameters):
        if len(parameters) == 0:
            return

        query = " ".join(parameters)

        response = requests.get(self._request_uri.format(query))
        data = json.loads(response.text)

        if data and data["list"] and len(data["list"]) > 0:
            channel.send_message(data["list"][0]["permalink"])
        else:
            channel.send_message("Nothing found for {}".format(query))
