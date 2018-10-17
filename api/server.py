import tornado.web
import tornado.ioloop

from api.handlers.bovinos_handler import BovinosHandler
from api.handlers.racas_handler import RacasHandler
from api.persistence import database


def run(port):
    database.connect()
    app = tornado.web.Application([
        (r'/bovino/(\d+)', BovinosHandler),
        (r'/bovino', BovinosHandler),
        (r'/raca', RacasHandler)
    ])
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
