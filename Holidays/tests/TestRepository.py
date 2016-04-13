from asyncio.test_utils import TestCase
from Domain.Holiday import Holiday
from Repository.Repository import Repository



import unittest


class TestRepository(unittest.TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.repository = Repository()
        holy1 = Holiday("1", "London", "seaside", 260)
        holy2 = Holiday("2", "Constanta", "seaside", 160)
        self.repository.addItem(holy1)
        self.repository.addItem(holy2)

    def test_add(self):
        holy3 = Holiday("3", "Chisinau", "city-break", 260)
        self.repository.addItem(holy3)
        self.assertEqual(len(self.repository.getAll()), 3)


def suite():
    ts = unittest.TestSuite()
    ts.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRepository))
    return ts
