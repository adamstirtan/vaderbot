def scream_loud(database, channel, params):
    import random

    word = " ".join(params)

    if len(word) > 50:
        channel.send_message("That's not a good idea.")
        return
    elif word == "":
        word = "BWAUGH"

    word = word.upper()

    channel.send_message((lambda w: w[0] + "".join(c * random.randint(1, 16) for c in word[1:]))(word))