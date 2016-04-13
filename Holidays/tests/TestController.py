from asyncio.test_utils import TestCase
from Controller.Controller import Controller
from Domain.Holiday import Holiday
from Repository.Repository import Repository


import unittest


class TestController(unittest.TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.repository = Repository()
        self.controller = Controller(self.repository)
        holy1 = Holiday("1", "London", "seaside", 260)
        holy2 = Holiday("2", "Constanta", "seaside", 160)
        holy3 = Holiday("3", "Chisinau", "city-break", 260)
        self.repository.addItem(holy1)
        self.repository.addItem(holy2)
        self.repository.addItem(holy3)

    def test_type(self):
        self.assertEqual(len(self.controller.filterByType("seaside")), 2)

    def test_resort(self):
        self.controller.filterByResort("London")
        self.assertEqual(len(self.controller.filterByResort("London")), 1)


def suite():
    ts = unittest.TestSuite()
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestController))
    return ts