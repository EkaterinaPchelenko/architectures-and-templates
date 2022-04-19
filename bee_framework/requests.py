from stuff import parse_data


class GetMethod:

    @staticmethod
    # @parse_data
    def get_params(environ):
        query_str = environ['QUERY_STRING']
        params = parse_data(query_str)
        return params


class PostMethod:

    @staticmethod
    def get_wsgi_data(env) -> bytes:
        cont_len_data = env.get('CONTENT_LENGTH')
        print(f'Длина: {type(cont_len_data)}')
        if cont_len_data:
            cont_len = int(cont_len_data)
        else:
            cont_len = 0
        print(cont_len)
        if cont_len > 0:
            data = env['wsgi.input'].read(cont_len)
        else:
            data = b''
        return data

    # @parse_data
    def parse_wsgi_data(self, data: bytes):
        if data:
            data_str = data.decode(encoding='utf-8')
            print(f'decoded str: {data_str}')
            params = parse_data(data_str)
            return params

    def get_params(self, environ):
        data = self.get_wsgi_data(environ)
        data = self.parse_wsgi_data(data)
        return data
