'''
Created on Dec 14, 2015

@author: AndiD
'''
import unittest

from unittest.suite import TestSuite
from test1 import TestAssignmentController, TestGradeController, TestMain, TestRepository, TestStudentController

if __name__ == "__main__":
    all_suites = [TestRepository.suite(), TestStudentController.suite(), TestAssignmentController.suite(),
                  TestGradeController.suite()]
    ts = TestSuite(all_suites)
    unittest.TextTestRunner(verbosity=2).run(ts)
