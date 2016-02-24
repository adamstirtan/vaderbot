from http.server import BaseHTTPRequestHandler


class BotRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        html = open("web/html/index.html").read()

        self.wfile.write(bytes(html, "utf8"))
        return
