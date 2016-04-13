import unittest
from unittest.case import TestCase
from contr.ControllerAssign import ControllerAssignment
from contr.ControllerUndoRedo import UndoController
from contr.ValidatorAssignment import ValidatorAssign
from exc.MyException import CustomException
from repository.Repository import Repository

__author__ = 'ecaterinacarazan'


class TestAssignmentController(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.controller = ControllerAssignment(Repository(), ValidatorAssign(), UndoController())
        # put here test logic
        self.controller.add_assignment(1, "ASC", "May")
        self.controller.add_assignment(2, "FP", "March")
        self.controller.add_assignment(3, "Logic", "April")

    # should follow controller tests
    # take care -> all functions should have prefix test_ compare
    def test_add(self):
        self.controller.add_assignment(4, "Algebra", "December")
        self.assertEqual(len(self.controller.get_all_assignments()), 4)
        try:
            self.controller.add_assignment(1, "Analysis", "January")
        except CustomException as e:
            self.assertEqual(e.get_msg(), "Can not add assignment with same id")

    def test_remove(self):
        self.controller.remove_assignment(1)
        self.assertEqual(len(self.controller.get_all_assignments()), 2)

    def test_update(self):
        self.controller.update_assignment(3, "Logic", "June")
        updated_student = self.controller.get_assignment(3)
        self.assertEqual(updated_student.get_deadline(), "June")

    def test_undo(self):
        self.controller.add_assignment(4, "Algebra", "December")
        self.controller.undo()
        self.assertEqual(len(self.controller.get_all_assignments()), 3)

    def test_redo(self):
        self.controller.add_assignment(4, "Algebra", "December")
        self.controller.undo()
        self.controller.redo()
        self.assertEqual(len(self.controller.get_all_assignments()), 4)


def suite():
    ts = unittest.TestSuite()
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAssignmentController))
    return ts

