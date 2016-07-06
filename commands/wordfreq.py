from commands.command import Command
from wordcloud import WordCloud


class WordFreqCommand(Command):

    def __init__(self, client, api_key):
        Command.__init__(self)
        self.client = client
        self.api_key = api_key

    def execute(self, channel, parameters):
        if len(parameters) > 1:
            channel.send_message("Usage: !wordcloud [user]")
            return
        elif len(parameters) == 0:
            words = "kenken kenken kenken kenken madl madl lewzer lewzer lazerbeast rhaydeo rhaydeo"
            data = WordCloud().generate(words).to_image().tobytes()

            result = self.client.api_call(
                "files.upload",
                token=self.api_key,
                content=data,
                filename="test",
                title="Does this work at all ?",
                channel="#general"
            )

            print(result)
        else:
            return
