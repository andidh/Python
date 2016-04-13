from Domain.Holiday import Holiday
from Holidays.src.Repository.Repository import Repository

__author__ = 'ecaterinacarazan'


class FileRepository(Repository):
    def __init__(self):
        """
        initialise the class FileRepository
        :return:
        """
        Repository.__init__(self)

    def read(self):
        """
        reads from a txt file
        :return: adds to the list of objects those read from file
        """
        file = open("/Users/ecaterinacarazan/PycharmProjects/files/holiday.txt", 'r')
        lines = file.read().splitlines()
        for line in lines:
            list = line.split(";")
            holiday = Holiday(int(list[0]), list[1], list[2], int(list[3]))
            Repository.addItem(self, holiday)
        file.close()

    def write(self):
        """
        write to file
        :return: gets every object from the list and writes in into the file
        """
        file = open("/Users/ecaterinacarazan/PycharmProjects/files/holiday.txt", 'w')
        for holy in Repository.getAll(self):
            line = str(holy.get_id()) + ";" + holy.get_city() + ";" + holy.get_type() + ";" + str(holy.get_price())
            file.write(line + "\n")
        file.close()

