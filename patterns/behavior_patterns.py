import jsonpickle as jsonpickle

from templator import render


class TempView:
    template_name = 'template.html'

    def get_data(self):
        return {}

    def get_template(self):
        return self.template_name

    def rendering(self):
        template_name = self.get_template()
        context = self.get_data()
        return '200 OK', render(template_name, **context)

    def __call__(self, request):
        return self.rendering()


class ListView(TempView):
    queryset = []
    template_name = 'list.html'
    context_obj_name = 'objects_list'

    def get_queryset(self):
        print(self.queryset)
        return self.queryset

    def get_obj_name(self):
        return self.context_obj_name

    def get_data(self):
        queryset = self.get_queryset()
        object_name = self.get_obj_name()
        context = {object_name: queryset}
        return context


class CreateView(TempView):
    template_name = 'create.html'

    @staticmethod
    def get_request_data(request):
        return request['data']

    def create_obj(self, data):
        pass

    def __call__(self, request):
        if request['method'] == 'POST':
            data = self.get_request_data(request)
            self.create_obj(data)

            return self.rendering()
        else:
            return super().__call__(request)


class FileWriter:
    def __init__(self, file):
        self.file = file

    def write(self, text):
        with open(self.file, 'a', encoding='utf-8') as file:
            file.write(f'{text}\n')


class ConsoleWriter:

    def write(self, text):
        print(text)


class Observer:
    def update(self, subj):
        pass


class Subject:
    def __init__(self):
        self.observers = []

    def notification(self):
        for observer in self.observers:
            observer.update(self)


class SMSNotifier(Observer):
    def update(self, subj):
        print('SMS-сообщение: присоединился', subj.users[-1].name)


class EmailNotifier(Observer):
    def update(self, subj):
        print('Email-сообщение: присоединился', subj.users[-1].name)


class BaseSerializer:
    def __init__(self, object):
        self.object = object

    def save(self):
        return jsonpickle.loads(self.object)

    @staticmethod
    def load(data):
        return jsonpickle.loads(data)