'''
Created on Dec 14, 2015

@author: AndiD
'''
class UndoController:
    def __init__(self):
        self._operations = []
        self._index = -1

    def add(self, controllers):
        self._operations.append(controllers)
        self._operations = self._operations[0:self._index + 2]
        self._index = len(self._operations) - 1

    def undo(self):
        if self._index < 0:
            return False
        for controller in self._operations[self._index]:
            controller.undo()
        self._index -= 1
        return True

    def redo(self):
        print("here")
        if self._index >= len(self._operations) -1:
            return False
        self._index += 1
        for controller in self._operations[self._index]:
            print("redo controller")
            controller.redo()
        return True

