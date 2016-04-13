'''
Created on Dec 14, 2015

@author: AndiD
'''
import unittest
from unittest.case import TestCase
from contr.ControllerStudent import ControllerStudent
from contr.ControllerUndoRedo import UndoController
from contr.ValidatorStudent import ValidatorStudent
from exc.MyException import CustomException
from repository.Repository import Repository


class TestStudentController(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.controller = ControllerStudent(Repository(), ValidatorStudent(), UndoController())
        # put here test logic
        self.controller.add_student(1, "A", 1)
        self.controller.add_student(2, "B", 2)
        self.controller.add_student(3, "C", 3)

    # should follow controller tests
    # take care -> all functions should have prefix test_ compare
    def test_add(self):
        self.controller.add_student(4, "D", 4)
        self.assertEqual(len(self.controller.get_all_students()), 4)
        try:
            self.controller.add_student(1, "E", 5)
        except CustomException as e:
            self.assertEqual(e.get_msg(), "Can not add student with same id")

    def test_remove(self):
        self.controller.remove_student(1)
        self.assertEqual(len(self.controller.get_all_students()), 2)

    def test_update(self):
        self.controller.update_student(3, "D", 3)
        updated_student = self.controller.get_by_id(3)
        self.assertEqual(updated_student.get_name(), "D")

    def test_undo(self):
        self.controller.add_student(4, "D", 4)
        self.controller.undo()
        self.assertEqual(len(self.controller.get_all_students()), 3)

    def test_redo(self):
        self.controller.add_student(4, "D", 4)
        self.controller.undo()
        self.controller.redo()
        self.assertEqual(len(self.controller.get_all_students()), 4)


def suite():
    ts = unittest.TestSuite()
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestStudentController))
    return ts
