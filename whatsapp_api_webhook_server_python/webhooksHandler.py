from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

from whatsapp_api_webhook_server_python.webhooks import Webhooks


class webhooksHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        length = self.headers['Content-Length']
        if length != None:
            content_length = int()
            body = self.rfile.read(content_length)
            Webhooks.webhookProccessing(body, self.onEvent)
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        dataBytes = self.rfile.read(content_length)
        dataText = dataBytes.decode("utf-8", 'ignore')
        Webhooks.webhookProccessing(dataText, self.onEvent)

    def do_DELETE(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        Webhooks.webhookProccessing(body, self.onEvent)
  
def startServer(host: str, port: int, onEvent):
    Handler = webhooksHandler
    Handler.onEvent = onEvent
    httpd = HTTPServer((host, port), Handler)
    httpd.serve_forever()