from http import HTTPStatus

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
        self.set_header("Content-Type", "application/json")

    def options(self):
        self.set_status(HTTPStatus.NO_CONTENT)
        self.finish()
