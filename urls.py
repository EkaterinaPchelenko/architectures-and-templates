from datetime import date
from views import Index, About, Date, Time, Contacts, TrainingPrograms, TrainingList, CreateTraining, CreateCategory, \
    CopyTraining, CategoryList


def secret_front(request):
    request['date'] = date.today()


def base_front(request):
    request['key'] = 'key'


fronts = [secret_front, base_front]


routes = {
    '/': Index(),
    '/about/': About(),
    '/contacts/': Contacts(),
    '/date/': Date(),
    '/time/': Time(),
    '/training_programs/': TrainingPrograms(),
    '/training_list/': TrainingList(),
    '/category_list/': CategoryList(),
    '/create_training/': CreateTraining(),
    '/create_category/': CreateCategory(),
    '/copy_training/': CopyTraining()
}