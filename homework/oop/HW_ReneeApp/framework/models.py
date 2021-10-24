"""
базовий абстракний клас для моделей
"""
from abc import ABC, abstractmethod
import json


class Model(ABC):
    file = "default.json"

    def save(self):
        obj_in_dict_format = self._generate_dict()
        obj = self.get_file_data(self.file)
        obj.append(obj_in_dict_format)
        self.save_to_file(obj)

    def _generate_dict(self):
        # return {attr: getattr(self, attr) for attr in vars(self)}
        return self.__dict__

    @classmethod
    def get_by_id(cls, id):
        data = cls.get_file_data(cls.file)
        for el in data:
            if el['id'] == id:
                return el
        raise Exception("Not found")

    @classmethod
    def get_all(cls):
        data = cls.get_file_data(cls.file)
        return data

    @staticmethod
    def get_file_data(file_name):
        file = open("database/" + file_name, 'r')
        data = json.loads(file.read())
        file.close()
        return data

    def save_to_file(self, data):
        data = json.dumps(data)
        file = open("database/" + self.file, 'w')
        file.write(data)
        file.close()
