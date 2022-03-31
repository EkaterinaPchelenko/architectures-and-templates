import time
from datetime import datetime

from bee_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


class About:
    def __call__(self, request):
        return '200 OK', 'Bee Framework'


class Time:
    def __call__(self, request):
        return '200 OK', f'{datetime.now().time()}'


class Date:
    def __call__(self, request):
        return '200 OK', f'{datetime.now().date()}'


class Error404:
    def __call__(self, request):
        return '404 WHAT', '404 Page Not Found'
