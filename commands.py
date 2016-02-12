import json
import requests


def urban_dictionary(client, channel_name, query):
    if len(query) == 0:
        return
    query = " ".join(query)
    response = requests.get("http://api.urbandictionary.com/v0/define?term={}".format(query))
    data = json.loads(response.text)
    if data is not None and data["list"] is not None and len(data["list"]) > 0:
        link = data["list"][0]["permalink"]
        try:
            channel = next(channel for channel in client.server.channels if channel.name == channel_name)
        except StopIteration:
            raise Exception("Could not find that channel")
        channel.send_message(link)
