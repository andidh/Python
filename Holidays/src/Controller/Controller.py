from operator import itemgetter
from Controller.ControllerException import ControllerException

__author__ = 'ecaterinacarazan'


class Controller:
    def __init__(self, repository):
        """
        initialise the class controller
        :param repository: the file repository of this controller
        :return:
        """
        self.repository = repository

    def filterByResort(self, city):
        """
        finds all the holidays belonging to a Resort
        :param city: the name of the Resort
        :return: the list of holidays of a type given
        """
        holidays = self.repository.getAll()
        holy_city = []
        for holy in holidays:
            if holy.get_city() == city:
                holy_city.append(holy)
        if holy_city == []:
            raise ControllerException("Wrong input")
        return holy_city

    def filterByType(self, type):
        """
        sorts ascending the list of holidays of a type given
        :param type: type of the holiday
        :return: the list of holidays of a type given
        """
        holidays = self.repository.getAll()
        holy_city = []
        for holy in holidays:
            if holy.get_type() == type:
                holy_city.append([holy.get_id(), holy.get_city(), holy.get_type(), holy.get_price()])
        holy_city = sorted(holy_city, key=itemgetter(3))
        return holy_city

    def read(self):
        """
        reads the list of holidays from a file
        :return:
        """
        self.repository.read()

    def write(self):
        """
        writes the list of holidays into a file
        :return:
        """
        self.repository.write()

    def get_all(self):
        """
        :return: all the holidays from the list
        """
        return self.repository.getAll()
