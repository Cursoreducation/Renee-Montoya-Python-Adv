from abc import ABC
import json


class Model(ABC):
    file = 'default.json'

    def save(self):
        general_dict_format = self._generate_dict()
        general = self.get_file_data(self.file)
        general.append(general_dict_format)
        self.save_to_file(general)

    def _generate_dict(self):
        return {select_values: getattr(self, select_values) for select_values in self.__dict__}

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
        return map(lambda el: cls(**el), data)
        # return data

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
