"""
Super Simple HTTP Server in Python .. not for production just for learning and fun
Author: Wolf Paulus (https://wolfpaulus.com), edited by Woramon P.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import asctime
from main import multiply_by_two_str
import json

hostName = "0.0.0.0"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/health":
            content_type = "text/html"
            status, content = 200, "OK"
        elif self.path == "/" or self.path.startswith("/?number="):
            status = 200
            number = self.path.split("=")[1] if self.path.startswith("/?number=") else ""
            result = multiply_by_two_str(number)

            # make the service respond when JSON is requested
            # https://gist.github.com/zuize47/370f33c2966b763eb16477bdfd71896a
            if self.headers.get('accept') == "application/json":
                content_type = "application/json"
                content = json.dumps({'response': result})
            else:
                content_type = "text/html"
                # in PyCharm, make sure working directory is /cicd/
                with open('./src/response.html', 'r') as f:
                    # read the html template and fill in the parameters: path, time and result
                    content = f.read().format(path=self.path, time=asctime(), result=result)
        else:
            content_type = "text/html"
            status, content = 404, "Not Found"
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()
        self.wfile.write(bytes(content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
