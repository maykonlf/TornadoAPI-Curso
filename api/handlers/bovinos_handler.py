import json
from http import HTTPStatus

from api.handlers.base_handler import BaseHandler
import tornado.escape

from api.persistence import database


class BovinosHandler(BaseHandler):
    def post(self):
        data = tornado.escape.json_decode(self.request.body)

        nome = data.get("nome")
        if not nome:
            self.set_status(HTTPStatus.BAD_REQUEST)
            return self.write('{"erro": "nome inválido"}')

        peso = data.get("peso")
        if not peso:
            self.set_status(HTTPStatus.BAD_REQUEST)
            return self.write('{"erro": "peso inválido"}')

        nascimento = data.get("nascimento")
        if not nascimento:
            self.set_status(HTTPStatus.BAD_REQUEST)
            return self.write('{"erro": "nascimento inválido"}')

        database.adicionar_bovino(data)
        self.set_status(HTTPStatus.CREATED)
        self.finish()

    def get(self, id=None):
        if id:
            bovino = database.consultar_bovino(id)
            if not bovino:
                self.set_status(HTTPStatus.NOT_FOUND)
                return
            else:
                self.set_status(HTTPStatus.OK)
                return self.write(json.dumps(bovino))
        else:
            lista = database.listar_bovinos()
            self.set_status(HTTPStatus.OK)
            self.write(json.dumps(lista))

    def put(self, id):
        data = tornado.escape.json_decode(self.request.body)
        nome = data.get("nome")
        if not nome:
            self.set_status(HTTPStatus.BAD_REQUEST)
            return self.write('{"erro": "nome inválido"}')

        peso = data.get("peso")
        if not peso:
            self.set_status(HTTPStatus.BAD_REQUEST)
            return self.write('{"erro": "peso inválido"}')

        nascimento = data.get("nascimento")
        if not nascimento:
            self.set_status(HTTPStatus.BAD_REQUEST)
            return self.write('{"erro": "nascimento inválido"}')

        bovino = database.consultar_bovino(id)
        if not bovino:
            self.set_status(HTTPStatus.NOT_FOUND)
            return self.finish()

        database.atualizar_bovino(id, data)
        self.set_status(HTTPStatus.NO_CONTENT)
        self.finish()

    def delete(self, id):
        bovino = database.consultar_bovino(id)
        if not bovino:
            self.set_status(HTTPStatus.NOT_FOUND)
            return self.finish()
        database.excluir_bovino(id)
        self.set_status(HTTPStatus.NO_CONTENT)
        self.finish()
