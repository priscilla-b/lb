from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import logging

HOST = "192.168.0.198"
PORT = 9999

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class LBHttpHandler(BaseHTTPRequestHandler):
    # LBHttp extends the BaseHTTPRequestHandler class

    def log_request_details(self):
        logging.info("Received request from {0}".format(self.client_address))
        logging.info("Headers: {0}".format(self.headers))


    # handles how to respond to get requests
    def do_GET(self):
        self.log_request_details()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>HELLO WORLD</h1></body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        self.wfile.write(bytes(f'{{"time":"{date}"}}', "utf-8"))



if __name__ == "__main__":
    try:

        server = HTTPServer((HOST, PORT), LBHttpHandler)
        print("Server running at http://{}:{}".format(HOST, PORT))
        server.serve_forever()
              
    except KeyboardInterrupt:
        print("\nServer is stopping...")
        server.server_close()
        print("Server stopped.")
