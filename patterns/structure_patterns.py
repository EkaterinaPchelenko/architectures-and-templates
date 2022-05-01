from time import time


class Route:
    def __init__(self, routes, url):
        self.routes = routes
        self.url = url

    def __call__(self, myclass):
        self.routes[self.url] = myclass()


class Debug:
    def __init__(self, name):
        self.name = name

    def __call__(self, myclass):

        def time_deco(method):
            def time_wrapper(*args, **kwargs):
                start = time()
                res = method(*args, **kwargs)
                end = time()
                res_time = end - start

                print(f'Debug: Время выполнения {self.name} - {res_time} ms')
                return res
            return time_wrapper
        return time_deco(myclass)