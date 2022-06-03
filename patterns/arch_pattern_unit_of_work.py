import threading


class UnitOfWork:
    current = threading.local()

    def __init__(self):
        self.new_obj = []
        self.used_obj = []
        self.removed_obj = []

    def set_registry(self, MapperRegistry):
        self.MapperRegistry = MapperRegistry

    def new_register(self, obj):
        self.new_obj.append(obj)

    def used_register(self, obj):
        self.used_obj(obj)

    def removed_register(self, obj):
        self.removed_obj(obj)

    def insert_new(self):
        print(self.new_obj)
        for obj in self.new_obj:
            print(f'Вывод {self.MapperRegistry}')
            self.MapperRegistry.get_mapper(obj).insert(obj)

    def update_used(self):
        for obj in self.used_obj:
            self.MapperRegistry.get_mapper(obj).update(obj)

    def delete_removed(self):
        for obj in self.removed_obj:
            self.MapperRegistry.get_mapper(obj).delete(obj)

    @staticmethod
    def new_current():
        __class__.set_current(UnitOfWork())

    @classmethod
    def set_current(cls, unit_of_work):
        cls.current.unit_of_work = unit_of_work

    @classmethod
    def get_current(cls):
        return cls.current.unit_of_work

    def commit(self):
        self.insert_new()
        self.update_used()
        self.delete_removed()
        self.new_obj.clear()
        self.used_obj.clear()
        self.removed_obj()


class DomainObj:
    def mark_new(self):
        UnitOfWork.get_current().new_register(self)

    def mark_used(self):
        UnitOfWork.get_current().used_register(self)

    def mark_removed(self):
        UnitOfWork.get_current().removed_registry(self)