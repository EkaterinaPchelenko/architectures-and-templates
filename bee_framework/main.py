import quopri

from requests import PostMethod, GetMethod


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

        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostMethod().get_params(environ)
            request['data'] = data
            print(f'Post-запрос: {Framework.decode_value(data)}')
        if method == 'GET':
            data = GetMethod().get_params(environ)
            request['request_params'] = data
            print(f'Get-запрос: {data}')
        print(request)

        if path in self.route_list:
            view = self.route_list[path]
        else:
            view = Error404()

        for f in self.front_list:
            f(request)
        code, info = view(request)
        start_resp(code, [('Content-Type', 'text/html')])
        return [info.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        info = {}
        for key, value in data.items():
            val = bytes(value.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            info[key] = val_decode_str
        return info
