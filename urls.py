from datetime import date
from views import Index, About, Contacts, TrainingPrograms, TrainingList, CreateTraining, CreateCategory, \
    CopyTraining, CategoryList


def secret_front(request):
    request['date'] = date.today()


def base_front(request):
    request['key'] = 'key'


fronts = [secret_front, base_front]


