import unittest
from unittest.case import TestCase
from contr.ControllerGrade import ControllerGrade
from contr.ControllerUndoRedo import UndoController
from contr.ValidatorGrade import ValidatorGrade
from exc.MyException import CustomException
from repository.Repository import Repository

__author__ = 'ecaterinacarazan'


class TestGradeController(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.controller = ControllerGrade(Repository(), Repository(), Repository(), ValidatorGrade(), UndoController())
        # put here test logic
        self.controller.add_grade(1, 1, 1, 9)
        self.controller.add_grade(2, 1, 2, 4)
        self.controller.add_grade(3, 1, 3, 3)

    def test_add(self):
        self.controller.add_grade(4, 1, 4, 8)
        self.assertEqual(len(self.controller.get_all_grades()), 4)
        try:
            self.controller.add_grade(1, 2, 2, 7)
        except CustomException as e:
            self.assertEqual(e.get_msg(), "Can not add grade with same id")

    def test_remove(self):
        self.controller.remove_grade(1)
        self.assertEqual(len(self.controller.get_all_grades()), 2)

    def test_update(self):
        self.controller.update_grade(3, 7)
        updated_student = self.controller.get_by_id(3)
        self.assertEqual(updated_student.get_grade(), 7)

    def test_undo(self):
        self.controller.add_grade(4, 1, 4, 8)
        self.controller.undo()
        self.assertEqual(len(self.controller.get_all_grades()), 3)

    def test_redo(self):
        self.controller.add_grade(4, 1, 4, 8)
        self.controller.undo()
        self.controller.redo()
        self.assertEqual(len(self.controller.get_all_grades()), 4)


def suite():
    ts = unittest.TestSuite()
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestGradeController))
    return ts

