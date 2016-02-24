import subprocess

def update(database, channel, params):
    channel.send_message("Restarting myself! Wait for a bit.")
    subprocess.call(["systemctl","restart","vaderbot.service"])

if __name__ == "__main__":
    update(None,None,None)
