import quopri


class Error404:
    def __call__(self, request):
        return '404 WHAT', '404 Page Not Found'


class Framework:
    def __init__(self, route_object, front_object):
        self.route_list = route_object
        self.front_list = front_object

    def __call__(self, environ, start_resp):
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.route_list:
            view = self.route_list[path]
        else:
            view = Error404()
        request = {}

        for f in self.front_list:
            f(request)
        code, info = view(request)
        start_resp(code, [('Content-Type', 'text/html')])
        return [info.encode('utf-8')]
