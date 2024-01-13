import tornado.ioloop
import tornado.web

from .webhooks import handle_notification


class WebhooksHandler(tornado.web.RequestHandler):
    def get(self):
        length = self.request.headers.get('Content-Length')
        if length is not None:
            handle_notification(self.request.body, self.onEvent)
        else:
            self.set_status(200)
            self.set_header('Content-type', 'text/html')

    def post(self):
        length = self.request.headers.get('Content-Length')
        if length is not None:
            handle_notification(self.request.body, self.onEvent)

    def delete(self):
        length = self.request.headers.get('Content-Length')
        if length is not None:
            handle_notification(self.request.body, self.onEvent)


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
