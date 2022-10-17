import tornado.ioloop
import tornado.web

from whatsapp_api_webhook_server_python.webhooks import Webhooks


class WebhooksHandler(tornado.web.RequestHandler):

    def get(self):
        length = self.request.headers.get('Content-Length')
        if length != None:
            dataBytes = self.request.body
            dataText = dataBytes.decode("utf-8", 'ignore')
            Webhooks.webhookProccessing(dataText, self.onEvent)
        else:
            self.set_status(200)
            self.set_header('Content-type', 'text/html')

    def post(self):
        length = self.request.headers.get('Content-Length')
        if length != None:
            dataBytes = self.request.body
            dataText = dataBytes.decode("utf-8", 'ignore')
            Webhooks.webhookProccessing(dataText, self.onEvent)

    def delete(self):
        length = self.request.headers.get('Content-Length')
        if length != None:
            dataBytes = self.request.body
            dataText = dataBytes.decode("utf-8", 'ignore')
            Webhooks.webhookProccessing(dataText, self.onEvent)
  
class Application(tornado.web.Application):
    def __init__(self, handler):
        handlers = [
            (r"/", handler),
        ]
        tornado.web.Application.__init__(self, handlers)

def startServer(host: str, port: int, onEvent, startLoop: bool = True):
    handler = WebhooksHandler
    handler.onEvent = onEvent
    http_server = tornado.httpserver.HTTPServer(Application(handler))
    http_server.listen(port=port, address=host)
    if startLoop:
        tornado.ioloop.IOLoop.instance().start()