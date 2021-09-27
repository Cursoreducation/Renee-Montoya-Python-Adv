import requests


class ClassForTest:
    def send_request(self):
        response = requests.get("http://jsonplaceholder.typicode.com/tsodos")
        return response
