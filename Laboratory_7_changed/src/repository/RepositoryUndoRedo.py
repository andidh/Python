from copy import deepcopy
from repository.Repository import Repository


class RepoUndoRedo(Repository):
    def __init__(self):
        Repository.__init__(self)
        self._history = []
        self._index = -1

    def add(self, item):
        self._history.append(deepcopy(self._items))
        Repository.add_item(self, item)
        self._history = self._history[0:self._index + 2]
        self._index = len(self._history) - 1
        self._history.pop()

    def remove(self, id):
        self._history.append(deepcopy(self._items))
        Repository.remove_item(self, id)
        self._history = self._history[0:self._index + 2]
        self._index = len(self._history) - 1
        self._history.pop()

    def update(self, item):
        self._history.append(deepcopy(self._items))
        Repository.update_item(self, item)
        self._history = self._history[0:self._index + 2]
        self._index = len(self._history) - 1
        self._history.pop()

    def undo(self):
        if self._index < 0:
            return False
        self._items = deepcopy(self._history[self._index])
        self._index -= 1
        return True

    def redo(self):
        if self._index < 0:
            return False
        # self._items = deepcopy()

    def print_his(self):
        print(self._history)

        #attention!