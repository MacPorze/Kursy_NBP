from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

@view_config(name='hello', request_method='GET')
def hello_world(request):
    return Response('Hello Maciejs!')

@view_config()
def main(request):
    return Response('MAIN')

if __name__ == '__main__':
    with Configurator() as config:
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()