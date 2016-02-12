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
    word = " ".join(params)
    if word == "":
        word = "BWAUGH"
    channel.send_message((lambda w: w[0] + "".join(c * randint(1, 8) for c in word[1:]))(word))


def scream_loud(channel, params):
    word = " ".join(params)
    if word == "":
        word = "BWAUGH"
    channel.send_message((lambda w: w[0] + "".join(c * randint(1, 16) for c in word[1:]))(word))
