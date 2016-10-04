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
        "There is a reasonable probability",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "How dare you talk to me",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful",
        ":soft_cock":,
        ":hard_cock:",
        "Zaboravi to",
        "You are feg"
    ]
    def __init__(self):
        Command.__init__(self)

    def execute(self, channel, parameters):
        if len(parameters) == 0:
            channel.send_message("Ask a question.")
            return
        separator = "" if parameters[-1].endswith("?") else "?"
        channel.send_message("{}{} {}.".format(" ".join(parameters), separator, random.choice(self.answers)))
