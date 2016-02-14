def urban_dictionary(channel, params):
    import requests
    import json

    if len(params) == 0:
        return

    query = " ".join(params)

    response = requests.get("http://api.urbandictionary.com/v0/define?term={}".format(query))
    data = json.loads(response.text)

    if data and data["list"] and len(data["list"]) > 0:
        channel.send_message(data["list"][0]["permalink"])
    else:
        channel.send_message("Nothing found for {}".format(query))
