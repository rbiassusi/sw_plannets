# -*- coding: utf-8 -*-
from tastypie.resources import ModelResource, ALL
from tastypie import fields
from ..models import Planeta
from tastypie.authorization import Authorization


class PlanetaResource(ModelResource):
    """
    Resource Planeta
    model: Planeta
    metodos: get, post e delete
    autorizacao: Nenhuma (aberto)
    """
    class Meta:
        resource_name = 'planeta'
        queryset = Planeta.objects.all()
        allowed_methods = ['get', 'post', 'delete']
        fields = ['nome', 'terreno', 'clima']
        authorization = Authorization()
        filtering = {
            'nome': ALL,
        }

    def dehydrate(self, bundle):
        bundle.data['id'] = bundle.obj.pk
        bundle.data['count_filmes'] = bundle.obj.count_filmes

        return bundle
