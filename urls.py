from datetime import date
from views import Index, About, Date, Time


def secret_front(request):
    request['data'] = date.today()


def base_front(request):
    request['key'] = 'key'


fronts = [secret_front, base_front]

routes = {
    '/': Index(),
    '/about/': About(),
    '/date/': Date(),
    '/time/': Time()  
}