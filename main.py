#!/usr/bin/env python3.5

from vader import Vader
from web.request_handler import BotRequestHandler
from http.server import HTTPServer
from threading import Thread


def main():
    server_address = ("127.0.0.1", 80)
    server = HTTPServer(server_address, BotRequestHandler)
    server_thread = Thread(target = server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    bot = Vader()
    bot.connect()

if __name__ == "__main__":
    main()
