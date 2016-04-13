'''
Created on Dec 14, 2015

@author: AndiD
'''
from repository.RepositoryException import RepositoryException


class Repository:
    def __init__(self):
        """
        initialise the repository with a void list of items
        :return:
        """
        self._items = []

    def set_items(self, items):
        self._items = items

    def get_all(self):
        """

        :return: all the items
        """
        return self._items

    def get_by_id(self, Id):
        """
        finds the item with the given id
        :param Id:
        :return:
        """
        for item in self._items:
            if item.get_id() == Id:
                return item
        return None

    def add_item(self, item):
        """
        adds an item
        :param item:
        :return:
        """
        self._items.append(item)

    def remove_item(self, item_id):
        """
        removes an item from the list
        :param item_id:
        :return:
        """
        for i in self._items:
            if i.get_id() == item_id:
                self._items.remove(i)
                return
        raise RepositoryException("No such item")

    def update_item(self, item):
        """
        updates an item from the list if found
        :param item:
        :return:
        """
        index = -1
        for i in range(len(self._items)):
            if self._items[i].get_id() == item.get_id():
                index = i
                break
        if index == -1:
            raise RepositoryException("No item for update found")
        else:
            self._items[index] = item
