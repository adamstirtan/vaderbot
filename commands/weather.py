def weather(database, channel, params):
    import requests
    import json

    if len(params) == 0:
        return


    query = " ".join(params)
    api_key = "44db6a862fba0b067b1930da0d769e98"

    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(query,api_key))
    data = json.loads(response.text)

    description = data['weather'][0]['description']
    # temp = data['temp']
    name = data['name']

    print(data)
    print("-----------------------------")
    print(description)
    # print(temp)
    print(name)
    # print("-----------------------------")
    # print (name,temp,description)
    # channel.send_message(name,temp,description)
