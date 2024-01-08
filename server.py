# Webサーバーを起動するプログラム
from http.server import HTTPServer, CGIHTTPRequestHandler

# class MyHandler(CGIHTTPRequestHandler):
#     def end_headers(self):
#         self.send_header('Content-Type', 'application/javascript; charset=utf-8')
#         super().end_headers()


httpd = HTTPServer(("127.0.0.1", 8080), CGIHTTPRequestHandler)
httpd.serve_forever()