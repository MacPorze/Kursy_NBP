from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config


from pyramid.response import Response

import db_service


@view_config(renderer='static\index.pt')
def main(request):
    return {}

@view_config(name='data', renderer='json')
def data(request):
    new_data = db_service.read()
    return new_data

@view_config(name='update')
def update(request):
    db_service.write()
    return Response('OK')

if __name__ == '__main__':
    with Configurator() as config:
        config.scan()
        config.include('pyramid_chameleon')
        config.add_static_view(name='static', path='static')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()