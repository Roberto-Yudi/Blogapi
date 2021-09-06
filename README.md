# About the project 
Este API é baseado no projeto ensinado no livro Django for APIs de William S Vincent
projeto original: https://github.com/wsvincent/restapiswithdjango
disponível em: https://sample-blogapi.herokuapp.com/api/v1
Docs disponível em: https://sample-blogapi.herokuapp.com/swagger/

## Features:
- DRF, Browsable API, Generic class-based Api views, 
- Permissão a nível de projeto, apenas usuarios logados tem acesso aos posts
- Permissão customizada, o usuario só tem permissão de edição ou remoção se for autor do post.
- Autenticação por token, em substituição da autenticação basica, complementar a autenticação por sessão,
- ViewSets, views de list e detail juntas em uma única viewset
- Routers, geração automatica de urls.
- Schemas, estatico e dinamico.
- Documentation, através do pacote drf-yasg

## Built with:
-	Django 3.2.

## Packages:
- djangorestframework 
- dj-rest-auth 
- django-allauth 
- pyyaml 
- uritemplate 
- drf-yasg 

## Obs:
projeto em andamento.