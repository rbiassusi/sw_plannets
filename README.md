# sw_plannets
API Star Wars planets

Requisitos
==========

Core
----
* Python 2.7
* Django nonrel 1.6 beta
* Tastypie
* MongoDB

Opcional
--------
* pip
* virtual_env 

Instalação
==========
* apt-get install mongodb-server python-mongoengine
* pip install -r requirements.txt
* pip install requests[security]
* pip install git+https://github.com/django-nonrel/django@nonrel-1.6-beta
* python manage.py syncdb

Teste
=====
* python manage.py test

Utilização
==========
Rodar o servidor django:
* python manage.py runserver


------

2. Acesso via API

* Endereço da API:
  /api/v1
  
* Endereço do Schema:
  /api/v1/planeta/schema/
  
* Endpoint contato:
  /api/v1/planeta/


