import requests
import json

from commands.command import Command
from fuzzywuzzy import fuzz


class LcboCommand(Command):

    def __init__(self):
        Command.__init__(self)

        self._api_key = "MDo2MTllZGY1YS1lMjQ3LTExZTUtYTc0OS1jZjM1YWRjZGE1NmE6ZmFkenBUUm0wZUNlbmlSQUVDeVZvd3JkOGxkUjFqVjNXQlgy"
        self._request_uri = "https://lcboapi.com/"

    def execute(self, channel, parameters):
        if len(parameters) == 0:
            channel.send_message("Usage: !lcbo [product]")
            return

        query = " ".join(parameters).lower()

        products_response = requests.get(self._request_uri + "products?per_page=100&access_key=" + self._api_key)
        data = json.loads(products_response.text)

        if data and data["result"] and len(data["result"]) > 0:
            for product in data["result"]:
                if product["name"] and fuzz.ratio(query, product["name"].lower()) > 90:
                    channel.send_message(product["image_thumb_url"])
                    channel.send_message("id: " + str(product["id"]) + " name: " + product["name"])
