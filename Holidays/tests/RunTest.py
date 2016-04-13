from Holidays.tests import TestRepository
from Holidays.tests import TestController
from unittest import TestSuite


import unittest


if __name__ == "__main__":
    all_suites = [TestRepository.suite(), TestController.suite()]
    ts = TestSuite(all_suites)
    unittest.TextTestRunner(verbosity=2).run(ts)
