import socketserver
import http.server
import time

PORT = 7575


class AlgoliaRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            return self.hello()

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def hello(self):
        print('Howdy world 👋')
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(str.encode("Hello world!"))


if __name__ == '__main__':
    # with socketserver.TCPServer(("", PORT), AlgoliaRequestHandler) as httpd:
    #     print("serving at port", PORT)
    #     httpd.serve_forever()


    httpd = socketserver.TCPServer(("", PORT), AlgoliaRequestHandler)
    print(time.asctime(), "Server Starts - %s:%s" % ("", PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % ("", PORT))
