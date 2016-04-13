from contr.ControllerException import ControllerException
from contr.UndoableOperations import AddOperation, RemoveOperation, UpdateOperation
from src.domain.Assignment import Assignment


class ControllerAssignment:
    """
    controller assignment
    """

    def __init__(self, repository, validator, controller_undo_redo):
        """
        initialize assignment controller
        :param repository: assignment repository
        :param validator: assignment validator
        :return:
        """
        self._repository = repository
        self._validator = validator
        self.controller_undo_redo = controller_undo_redo
        self._operations = []
        self._index = 0

    def get_all_assignments(self):
        """
        :return: all assignments
        """
        return self._repository.get_all()

    def set_assign(self, list):
        """
        set the assign list to the one given
        :param list:
        :return:
        """
        self._repository.set_items(list)

    def add_assignment(self, id_assign, description, deadline):
        """
        Adds an assignment to the list of assignments

        :param id_assign: positive integer
        :param description: string
        :param deadline: string
        :return:
        """
        assign = Assignment(id_assign, description, deadline)
        self._validator.validate_assignment(assign)
        for asgn in self._repository.get_all():
            if asgn.get_id() == id_assign:
                raise ControllerException("Can not add assignment with same id")
        self._repository.add_item(assign)
        self._operations.append(AddOperation(assign))
        self._index += 1
        self.controller_undo_redo.add([self])

    def remove_assignment(self, assign_id):
        """
        Removes an assignment from the list of assignments

        :param assign_id: positive integer
        :return:
        """
        assign = self.get_assignment(assign_id)
        self._repository.remove_item(assign_id)
        self._operations.append(RemoveOperation(assign))
        self._index += 1
        self.controller_undo_redo.add([self])

    def update_assignment(self, id_assign, description, deadline):
        """
        Finds the assignment with the same id and changes the rest of the fields with the new values

        :param id_assign: positive integer
        :param description: string
        :param deadline: string
        :return:
        """
        assign = Assignment(id_assign, description, deadline)
        self._validator.validate_assignment(assign)
        self._repository.update_item(assign)
        new_assign = self.get_assignment(id_assign)
        self._operations.append(UpdateOperation(assign, new_assign))
        self._index += 1
        self.controller_undo_redo.add([self])

    def get_assignment(self, id_assign):
        """
        finds the assignment with the id given
        """
        return self._repository.get_by_id(id_assign)

    def read(self):
        self._repository.reading()

    def write(self):
        self._repository.writing()

    def undo(self):
        if self._index == 0:
            return False

        self._index -= 1
        operation = self._operations[self._index]

        if isinstance(operation, AddOperation):
            self._repository.remove_item(operation.get_item().get_id())
        elif isinstance(operation, RemoveOperation):
            self._repository.add_item(operation.get_item())
        elif isinstance(operation, UpdateOperation):
            self._repository.update_item(operation.get_old())
        else:
            self._index +=1

    def redo(self):
        if self._index >= len(self._operations):
            return False

        operation = self._operations[self._index]
        if isinstance(operation, AddOperation):
            self._repository.add_item(operation.get_item())
            self._index +=1
        elif isinstance(operation, RemoveOperation):
            self._repository.remove_item(operation.get_item().get_id())
            self._index +=1
        elif isinstance(operation, UpdateOperation):
            self._repository.update_item(operation.get_updated())
            self._index +=1
        else:
            self._index -= 1




