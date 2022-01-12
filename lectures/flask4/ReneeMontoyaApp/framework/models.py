from abc import ABC, abstractmethod
import json


class Model(ABC):
    file = 'default.json'


    def save(self):
        pass

    def _generate_dict(self):
        pass

    def get_by_id(cls, id):
        data = cls.get_file_data(cls.file)
        for el in data:
            if el['id'] == id:
                return el

        raise Exception("Not found")

    def update_by_id(cls, id, data):
        items = cls.get_file_data(cls.file)
        for i in range(len(items)):
            if items[i]['id'] == id:
                items[i] = data
                break
        cls.save_to_file(items)

    def delete_by_id(cls, id):
        items = cls.get_file_data(cls.file)
        for i in range(len(items)):
            if items[i]['id'] == id:
                del items[i]
                break
        cls.save_to_file(items)

    def get_all(cls):
        data = cls.get_file_data(cls.file)
        return data

    def get_file_data(file_name):
        file = open("database/" + file_name, 'r')
        data = json.loads(file.read())
        file.close()
        return data

    def save_to_file(cls, data):
        data = json.dumps(data)
        file = open('database/' + cls.file, "w")
        file.write(data)
        file.close()
