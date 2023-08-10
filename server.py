# Webサーバーを起動するプログラム
from http.server import HTTPServer, CGIHTTPRequestHandler

httpd = HTTPServer(("127.0.0.1", 8080), CGIHTTPRequestHandler)
httpd.serve_forever()