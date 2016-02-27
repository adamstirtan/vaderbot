#!/usr/bin/env python3.5

from vader import Vader
from database.database_upgrader import DatabaseUpgrader
from web.request_handler import BotRequestHandler
from http.server import HTTPServer
from threading import Thread


def main():
    DatabaseUpgrader().upgrade()

    server = HTTPServer(("0.0.0.0", 80), BotRequestHandler)
    server_thread = Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    bot = Vader()
    bot.connect()

if __name__ == "__main__":
    main()
