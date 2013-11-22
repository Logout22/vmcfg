#! /usr/bin/python3.3

import http.server

httpd = http.server.HTTPServer(
    ("10.93.48.1", 8080),
    http.server.SimpleHTTPRequestHandler)

#httpd.handle_request()
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nKeyboard interrupt received, exiting.")
    httpd.server_close()

