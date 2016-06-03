import subprocess

from commands.command import Command

restart_commands = {
    "systemd": "systemctl restart vaderbot.service",
    "upstart": "restart vaderbot"
}

class UpdateCommand(Command):

    def __init__(self):
        Command.__init__(self)
        self._restart_command = self._check_systemd_or_upstart()
        print(self._restart_command)

    def execute(self, channel, parameters):
        channel.send_message("Restarting myself! Wait for a bit.")
        subprocess.call(self._restart_command, shell=True)

    def _check_systemd_or_upstart(self):
        import os
        service_type = "systemd"
        try:
            os.stat("/etc/systemd")
        except FileNotFoundError as e:
            service_type = "upstart"
        return restart_commands[service_type]
