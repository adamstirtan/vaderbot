from commands.command import Command
import random

class EightBallCommand(Command):
    answers = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes, definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    ]
    def __init__(self):
        Command.__init__(self)

    def execute(self, channel, parameters):
        if len(parameters) == 0:
            channel.send_message("Ask a question.")
            return
        channel.send_message("{}: {}.".format(" ".join(parameters), random.choice(self.answers)))
