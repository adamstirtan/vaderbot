def weather(database, channel, params):
    import requests
    import json
    import math

    if len(params) == 0:
        return


    query = " ".join(params)
    api_key = "44db6a862fba0b067b1930da0d769e98"

    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(query,api_key))
    data = json.loads(response.text)

    weather = "{} {} {}{} {}".format(data['name'],math.trunc(data['main']['temp']-273.15), "\N{DEGREE SIGN}","C " , data['weather'][0]['description'])

    print(weather)

    channel.send_message(weather)

# weather(None,None,"burlington")
