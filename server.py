from http.server import BaseHTTPRequestHandler
from Routes.router import routes
import sqlite3

class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_GET(self):
        self.respond()

    def do_POST(self):
        return

    def handle_http(self, status, content_type):
        self.send_response(status)
        self.send_header('Content - type', content_type)
        self.end_headers()

        if self.path in routes.keys():
            route_content = routes[self.path]
            route_content()
        else:
            r = self.path.split("/")
            route_content = routes[r[:-1].join("/")]
            user_id = r[-1]
            route_content(user_id)
        return bytes(route_content, "UTF - 8")

    def respond(self):
        content = self.handle_http(200, 'text / html')
        self.wfile.write(content)