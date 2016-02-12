import json
import requests
from random import randint


def urban_dictionary(channel, params):
    if len(params) == 0:
        return
    query = " ".join(params)
    response = requests.get("http://api.urbandictionary.com/v0/define?term={}".format(query))
    data = json.loads(response.text)
    if data and data["list"] and len(data["list"]) > 0:
        link = data["list"][0]["permalink"]
        channel.send_message(link)


def scream(channel, params):
    channel.send_message("B{}{}{}{}{}".format(
                         randint(1, 4) * "W",
                         randint(1, 8) * "A",
                         randint(1, 8) * "U",
                         randint(1, 8) * "G",
                         randint(1, 4) * "H"))


def scream_loud(channel, params):
    channel.send_message("B{}{}{}{}{}".format(
                         randint(1, 8) * "W",
                         randint(1, 16) * "A",
                         randint(1, 16) * "U",
                         randint(1, 16) * "G",
                         randint(1, 8) * "H"))
