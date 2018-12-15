# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from tastypie.api import Api
from sw_plannets.api.resources import PlanetaResource


v1_api = Api(api_name='v1')
v1_api.register(PlanetaResource())

urlpatterns = [
    url(r'^api/', include(v1_api.urls)),
]
