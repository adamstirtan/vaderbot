#!/usr/bin/env python3.5

from vader import Vader
from web.request_handler import BotRequestHandler
from http.server import HTTPServer


def main():
    server_address = ("127.0.0.1", 80)
    server = HTTPServer(server_address, BotRequestHandler)
    server.serve_forever()

    bot = Vader()
    bot.connect()

if __name__ == "__main__":
    main()
