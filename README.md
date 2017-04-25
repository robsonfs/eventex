# Eventex

[![Build Status](https://travis-ci.org/robsonfs/eventex.svg?branch=master)](https://travis-ci.org/robsonfs/eventex) [![Code Health](https://landscape.io/github/robsonfs/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/robsonfs/eventex/master)


Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as depedências
5. Configure a Instância com o .env
6. Execute os testes.

```console
git clone git@github.com:robsonfs/eventex.git wttd
cd wttd
python -m virtualenv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```
## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instancia
4. Defina DEBUG = False
5. Configure o serviço de e-mail
6. Enfie o código para o heroku

```console
heroku create minhainstancia
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# Configuro o e-mail
git push heroku master --force
```
