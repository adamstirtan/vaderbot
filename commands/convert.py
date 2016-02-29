import json
import requests
import math

from commands.command import Command


class ConvertCommand(Command):

    def __init__(self):
        Command.__init__(self)

    def execute(self, channel, parameters):
        if len(parameters) == 3:
            source = parameters[0]
            dest = parameters[1]

            try:
                amount = float(parameters[2])
            except ValueError:
                if parameters[2] == 'π':
                    amount = math.pi
                else:
                    amount = 0.0

            response = requests.get("http://api.fixer.io/latest?base={}&symbols={}".format(source, dest))

            info = json.loads(response.content.decode("utf8"))

            if not "error" in info and "rates" in info:
                if dest in info["rates"]:
                    message = "{:.2f}{} = {:.2f}{}".format(amount, source, info["rates"][dest] * amount, dest)
                else:
                    message = "Something isn't right."
            else:
                message = "Something isn't right."

            channel.send_message(message)
        else:
            channel.send_message("Usage: !convert [currency from] [currency to] [amount]")
