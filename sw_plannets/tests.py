# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from models import Planeta
import json


class TestCase(TestCase):
    """
    Realiza o teste utilizando request a API e avaliando seu retorno
    """

    def setUp(self):
        self.c = Client()

    def test_planeta_api(self):
        """
        teste da api:
        1- Insere um planeta (ficticio) e verifica o status_code retornado
        2- Insere outro planeta (existente) e verifica se não veio status_code diferente
        3- Faz um GET e verifica se o retorno da API corresponde com o numero de contatos inseridos (2)
        4- guarda a ID do segundo contato inserido
        5- faz um GET no planeta existente para confirmar o valor de filmes em que apareceu
        6- Deleta esse id do planeta ficticio
        7- Verifica se a contagem de planetas esta correta (1)
        """
        response = self.c.post("/api/v1/planeta/", json.dumps({"nome": "Teste 1",
                                                               "clima": "clima teste", "terreno": "terreno teste"}), content_type="application/json")

        self.assertEqual(response.status_code, 201)

        response = self.c.post(
            "/api/v1/planeta/", json.dumps({"nome": "Dagobah", "clima": "murky", "terreno": "swamp, jungles"}), content_type="application/json")
        self.assertNotEqual(response.status_code, 400)

        response = self.c.get("/api/v1/planeta/")

        objects = json.loads(response.content)["objects"]

        self.assertEqual(len(objects), 2)
        self.assertEqual(objects[0]["nome"], "Teste 1")
        self.assertEqual(objects[1]["nome"], "Dagobah")

        id_1 = objects[1]["id"]
        id_0 = objects[0]["id"]
        response = self.c.get("/api/v1/planeta/%s/" % id_1)

        obj = json.loads(response.content)

        self.assertEqual(obj['count_filmes'], 3)

        self.c.delete("/api/v1/planeta/%s/" % id_0)

        response = self.c.get("/api/v1/planeta/")
        objects = json.loads(response.content)["objects"]
        self.assertNotEqual(len(objects), 2)
        self.assertEqual(len(objects), 1)
