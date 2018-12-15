from django.db import models
import requests

SW_BASE_URL = "https://swapi.co/api/"
SW_RESOURCE = "planets/"


class Planeta(models.Model):
    nome = models.CharField(max_length=256)
    clima = models.CharField(max_length=128)
    terreno = models.CharField(max_length=64)

    # TODO: gravar no campo a qtd assim que o obj for criado, atualizar a cada
    # filme novo.
    @property
    def count_filmes(self):
        api_url_request = "%s%s?search=%s" % (
            SW_BASE_URL, SW_RESOURCE, self.nome)

        response = requests.get(api_url_request)
        data = response.json()
        if data['results']:
            return len(data['results'][0]['films'])

        return 0
