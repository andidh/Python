__author__ = 'ecaterinacarazan'


class Repository:
    def __init__(self):
        """
        initialise the class Repository
        :return: adds objects to the list and returns the list
        """
        self.items = []

    def addItem(self, item):
        """
        adds an item to the list
        :param item:
        :return:
        """
        self.items.append(item)

    def getAll(self):
        """
        :return: all the items from the list
        """
        return self.items

