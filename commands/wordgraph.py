from commands.command import Command
from PIL import Image, ImageDraw


class WordGraphCommand(Command):

    def __init__(self, message_repository):
        Command.__init__(self)

        self._message_repository = message_repository

    def execute(self, channel, parameters):
        if len(parameters) != 1:
            channel.send_message("Usage: !wordgraph [name]")
            return

        messages = self._message_repository.where("user = '{}'".format(parameters[0]))

        buffer = Image.new("RGBA", (1600, 1200))
        draw = ImageDraw.Draw(buffer)

        draw.line((0, 0) + buffer.size, fill=128)
        draw.line((0, buffer.size[1], buffer.size[0], 0), fill=128)

        del draw

        #buffer.save("C:/Users/adamstirtan/Desktop/wordgraph.bmp")
