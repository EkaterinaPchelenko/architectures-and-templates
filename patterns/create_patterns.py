import copy
import quopri

from patterns.behavior_patterns import Subject


class User:
    pass


class Trainer(User):
    pass


class SimpleUser(User):
    def __init__(self, name):
        self.trainings = []
        super().__init__(name)


class UsFactory:
    types = {
        'trainer': Trainer,
        'simple_user': SimpleUser
    }

    @classmethod
    def create(cls, type_):
        return cls.types[type_]()


class TrainingPrortotype:

    def clone(self):
        return copy.deepcopy(self)


class Training(TrainingPrortotype, Subject):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.trainings.append(self)
        self.users = []
        super().__init__()

    def __getitem__(self, item):
        return self.users[item]

    def add_user(self, user: SimpleUser):
        self.users.append(user)
        user.trainings.append(self)
        self.notification()


class RealTraining(Training):
    pass


class VideoTraining(Training):
    pass


class Category:
    auto_id = 0

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.trainings = []

    def trainings_amount(self):
        res = len(self.trainings)
        if self.category:
            res += self.category.trainings_amount()
        return res


class TrainingsFactory:
    types = {
        'real_training': RealTraining,
        'video_training': VideoTraining
    }

    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


class Engine:
    def __init__(self):
        self.trainers = []
        self.simple_users = []
        self.trainings = []
        self.categories = []

    @staticmethod
    def create_user(type_, name):
        return UsFactory.create(type_, name)

    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)

    def find_category(self, id):
        for cat in self.categories:
            print('item', cat.id)
            if cat.id == id:
                return cat
        raise Exception(f'Категории с id:{id} не существует!')

    @staticmethod
    def create_training(type_, name, category):
        return TrainingsFactory.create(type_, name, category)

    def get_training(self, name):
        for training in self.trainings:
            if training.name == name:
                return training
        return None

    def get_user(self, name) -> SimpleUser:
        for user in self.simple_users:
            if user.name == name:
                return user

    @staticmethod
    def decode_value(value):
        value_b = bytes(value.replace('%', '=').replace("+", " "), 'UTF-8')
        value_decode_str = quopri.decodestring(value_b)
        return value_decode_str.decode('UTF-8')


class Singleton(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']

        if name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]


class Logger(metaclass=Singleton):

    def __init__(self, name):
        self.name = name

    @staticmethod
    def logger(text):
        print('LOG--->', text)






