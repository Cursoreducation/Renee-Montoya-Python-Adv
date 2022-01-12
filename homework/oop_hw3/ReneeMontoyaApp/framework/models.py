from abc import ABC, abstractmethod
import json


class Model(ABC):
    file = 'default.json'

    # def _generate_dict(self):
    #     return {field: getattr(self, field) for field in self.__dict__}
    def _generate_dict(self):
        return self.__dict__

    def save(self):
        object_in_dict_format = self._generate_dict()
        objects = self.get_file_data(self.file)
        objects.append(object_in_dict_format)
        self.save_to_file(objects)

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
        file = open('database/' + self.file, "w")
        file.write(data)
        file.close()
