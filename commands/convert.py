import json
import requests

def convert(database, channel, params):
    if len(params) == 3:
        source = params[0]
        dest = params[1]
        amount = float(params[2])

        response = requests.get("http://api.fixer.io/latest?base={}&symbols={}".format(source,dest))

        info = json.loads(response.content.decode("utf8"))

        if not "error" in info and "rates" in info:
            if dest in info["rates"]:
                message = "{:.2f}{} = {:.2f}{}".format(amount,source,info["rates"][dest]*amount,dest)
            else:
                message = "Something isn't right."
        else:
            message = "Something isn't right."

        channel.send_message(message)
    else:
        channel.send_message("Usage: !convert [currency from] [currency to] [amount]")

if __name__ == "__main__":
    convert(None,None,["EUR","CAD","1"])
