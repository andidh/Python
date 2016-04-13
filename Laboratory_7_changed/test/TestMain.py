import unittest

from unittest.suite import TestSuite
from test import TestRepository
from test import TestStudentController
from test import TestAssignmentController
from test import TestGradeController

if __name__ == "__main__":
    all_suites = [TestRepository.suite(), TestStudentController.suite(), TestAssignmentController.suite(),
                  TestGradeController.suite()]
    ts = TestSuite(all_suites)
    unittest.TextTestRunner(verbosity=2).run(ts)
