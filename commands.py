import json
import requests


def urban_dictionary(client, query):
    if query == "":
        return
    response = requests.get("http://api.urbandictionary.com/v0/define?term={}".format(query))
    data = json.loads(response.text)
    if data is not None and data["list"] is not None and len(data["list"]) > 0:
        definition = data["list"][0]["definition"]
        client.rtm_send_message(channel="#general", message=definition)


