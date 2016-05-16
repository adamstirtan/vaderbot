import requests
import json

from commands.command import Command
from math import trunc


class WeatherCommand(Command):

    def __init__(self):
        Command.__init__(self)

        self._request_uri = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
        self._api_key = "44db6a862fba0b067b1930da0d769e98"

    def validate(self, parameters):
        if len(parameters) == 0:
            return False
        return True

    def create_output(self, parameters):
        pass

    def execute(self, channel, parameters):
        if len(parameters) == 0:
            return

        query = " ".join(parameters)

        try:
            response = requests.get(self._request_uri.format(query, self._api_key))
            print(response.text)
            if response.status_code == 200:
                data = json.loads(response.text)
                weather = "{} {}\N{DEGREE SIGN}C {}".format(data['name'],
                                                            trunc(data['main']['temp'] - 273.15),
                                                            data['weather'][0]['description'])
            else:
                weather = "I don't know!"
        except Exception as e:
            print(e)
            weather = "I don't know!"

        channel.send_message(weather)
