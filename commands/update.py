import subprocess

from commands.command import Command


class UpdateCommand(Command):

    def __init__(self):
        Command.__init__(self)

    def execute(self, channel, parameters):
        channel.send_message("Restarting myself! Wait for a bit.")
        subprocess.call(["systemctl", "restart", "vaderbot.service"])
