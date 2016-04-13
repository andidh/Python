'''
Created on Dec 14, 2015

@author: AndiD
'''
import unittest
from unittest.case import TestCase
from domain.Student import Student
from exc.MyException import CustomException
from repository.Repository import Repository


class TestRepository(unittest.TestCase):
    def setUp(self):
        # setUp method will be executed before every test
        TestCase.setUp(self)
        self.repository = Repository()
        # add mock students to repo
        stud1 = Student(1, "A", 1)
        stud2 = Student(2, "B", 2)
        stud3 = Student(3, "C", 3)
        self.repository.add_item(stud1)
        self.repository.add_item(stud2)
        self.repository.add_item(stud3)

    def test_add(self):
        self.repository.add_item(Student(4, "D", 4))
        self.assertEqual(len(self.repository.get_all()), 4)

    def test_remove(self):
        self.repository.remove_item(1)
        self.assertEqual(len(self.repository.get_all()), 2)
        # check for exception call
        try:
            self.repository.remove_item(4)
        except CustomException as e:
            self.assertEqual(e.get_msg(), "No such item")

    def test_update_student(self):
        self.repository.update_item(Student(1, "D", 2))
        updated_student = self.repository.get_by_id(1)
        self.assertEqual(updated_student.get_name(), "D")
        # check exception case
        try:
            self.repository.update_item(Student(4, "D", 4))
        except CustomException as e:
            self.assertEqual(e.get_msg(), "No item for update found")

    def test_get_by_id(self):
        stud1 = self.repository.get_by_id(1)
        self.assertEqual(stud1.get_name(), "A")
        stud2 = self.repository.get_by_id(4)
        self.assertIsNone(stud2)


def suite():
    ts = unittest.TestSuite()
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRepository))
    return ts
