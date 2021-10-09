import unittest
from plant import Employee

class Test1(unittest.Testcase):
    def setUp(self):
         self.employee = Employee(1, 'Test', 'Test', 'Test', 1)

    def test_as_dict(self):
         self.assertIn(self.get_plant_by_director_id == "John")



    def test_department(self):
         self.assertIn(self.department_id != None)

    def test_plant(self):
        self.assertIn(self.Employee.department == self.Plant)
