import time
from datetime import datetime, date

from bee_framework.templator import render
from patterns.create_patterns import Engine, Logger
from patterns.structure_patterns import Route, Debug

site = Engine()
logger = Logger('main')
routes = {}


@Route(routes=routes, url='/')
class Index:
    @Debug(name='Index')
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('data', None))


@Route(routes=routes, url='/contacts/')
class Contacts:
    @Debug(name='Contacts')
    def __call__(self, request):
        return '200 OK', render('contacts.html', data=request.get('data', None))


@Route(routes=routes, url='/about/')
class About:
    @Debug(name='About')
    def __call__(self, request):
        return '200 OK', 'Bee Framework'


@Route(routes=routes, url='/training_programs/')
class TrainingPrograms:
    @Debug(name='TrainingPrograms')
    def __call__(self, request):
        return '200 OK', render('training_programs.html', data=date.today())


class Error404:
    @Debug(name='Error404')
    def __call__(self, request):
        return '404 WHAT', '404 Page Not Found'


@Route(routes=routes, url='/training_list/')
class TrainingList:
    @Debug(name='TrainingList')
    def __call__(self, request):
        logger.logger('Список тренеровок')
        try:
            category = site.find_category(int(request['request_params']['id']))
            return '200 OK', render('training_list.html', objects_lst=category.trainings, name=category.name, id=category.id)
        except KeyError:
            return '200 OK', 'Тренировки ещё не были добавлены'


@Route(routes=routes, url='/create_training/')
class CreateTraining:
    category_id = -1

    @Debug(name='CreateTraining')
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category(int(self.category_id))
                training = site.create_training('video_training', name, category)
                site.trainings.append(training)
            return '200 OK', render('training_list.html', object_lst=category.trainings, name=category.name, id=category.id)
        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category(int(self.category_id))
                return '200 OK', render('create_training.html', name=category.name, id=category.id)
            except KeyError:
                return '200 OK', 'Категории ещё не были добавлены'


@Route(routes=routes, url='/create_category/')
class CreateCategory:
    @Debug(name='CreateCategory')
    def __call__(self, request):
        if request['method'] == 'POST':
            print(request)
            data = request['data']
            name = data['name']
            name = site.decode_value(name)
            category_id = data.get('category_id')
            category = None

            if category_id:
                category = site.find_category(int(category_id))
            new_category = site.create_category(name, category)
            site.categories.append(new_category)

            return '200 OK', render('index.html', objects_lst=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create_category.html', categories=categories)


@Route(routes=routes, url='/category_list/')
class CategoryList:
    @Debug(name='CategoryList')
    def __call__(self, request):
        logger.logger('Список категорий')
        return '200 OK', render('category_list.html', objects_lst=site.categories)


@Route(routes=routes, url='/copy_training/')
class CopyTraining:
    @Debug(name='CopyTraining')
    def __call__(self, request):
        request_params = request['request_params']
        try:
            name = request_params['name']
            old_training = site.get_training(name)
            if old_training:
                new_name = f'new_{name}'
                new_training = old_training.clone()
                new_training.name = new_name
                site.trainings.append(new_training)

            return '200 OK', render('training_list.html', objects_lst=site.trainings)
        except KeyError:
            return '200 OK', 'Тренировки ещё не были добавлены'



