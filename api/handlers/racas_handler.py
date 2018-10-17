import json

from api.handlers.base_handler import BaseHandler
from api.persistence import database


class RacasHandler(BaseHandler):
    def get(self):
        racas = database.listar_racas()
        self.write(json.dumps(racas))
