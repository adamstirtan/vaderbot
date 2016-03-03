import json
import requests
import math

try:
    from commands.command import Command
except ImportError:
    from command import Command


class ConvertCommand(Command):

    def __init__(self):
        Command.__init__(self)
        self._request_uri = "http://api.fixer.io/latest?base={}&symbols={}"

    def validate(self, parameters):
        if len(parameters) == 3:
            return True
        return False

    def create_output(self, parameters):
        src, dst, amount = parameters

        try:
            amount = float(amount)
        except ValueError:
            if parameters[2] == 'π':
                amount = math.pi
            else:
                return ":("

        return self._get_conversion(src, dst, amount)

    def execute(self, channel, parameters):
        if self.validate(parameters):
            message = self.create_output(parameters)
        else:
            message = "Usage: !convert [source currency] [destination currency] [amount]"

        channel.send_message(message)

    def _get_conversion(self, src, dst, amount):
        response = requests.get(self._request_uri.format(src, dst))
        info = json.loads(response.text)

        if not "error" in info and "rates" in info and dst in info["rates"]:
            message = "{:.2f}{} = {:.2f}{}".format(amount, src, info["rates"][dst] * amount, dst)
        else:
            message = "You done goofed."

        return message

if __name__ == "__main__":
    from fakechannel import FakeChannel

    channel = FakeChannel()

    converter = ConvertCommand()
    converter.execute(channel,["USD","CAD","1"])
