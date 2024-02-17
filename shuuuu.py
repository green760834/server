from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "fille not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'ulf-8'))

httpd = HTTPServer(('127.0.0.1', 8081), Serv)
print('Done!')
httpd.serve_forever()
#прокси сервер,днс сервер,

