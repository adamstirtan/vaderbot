import requests
import json
import math

def weather(database, channel, params):
    if len(params) == 0:
        return

    query = " ".join(params)
    api_key = "44db6a862fba0b067b1930da0d769e98"

    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(query,api_key))

    if response.status_code == 200:
        data = json.loads(response.text)
        weather = "{} {}\N{DEGREE SIGN}C {}".format(data['name'],math.trunc(data['main']['temp']-273.15), data['weather'][0]['description'])
    else:
        weather = "I don't know!"

    channel.send_message(weather)

