from copy import deepcopy
from contr.ControllerException import ControllerException
from contr.UndoableOperations import AddOperation, RemoveOperation, UpdateOperation
from domain.Student import Student


class ControllerStudent:
    """
    The student controller
    """
    def __init__(self, repository, validator, controller_undo_redo):
        """
        initialize the student controller

        :param repository: student repository
        :param validator: student validator
        """
        self._repository = repository
        self._validator = validator
        self.controller_undo_redo = controller_undo_redo
        self._operations = []
        self._index = 0

    def get_all_students(self):
        """
        :return: all students
        """
        return self._repository.get_all()

    def set_students(self, list):
        """
        set the list of students to a special value
        :param list:
        :return:
        """
        self._repository.set_items(list)

    def add_student(self, student_id, name, group):
        """
        Adds a student to the list of students

        :param student_id: positive integer
        :param name: string
        :param group: positive integer
        :return:
        """
        student = Student(student_id, name, group)
        self._validator.validate_student(student)
        for stud in self._repository.get_all():
            if stud.get_id() == student_id:
                raise ControllerException("Can not add student with same id")
        self._repository.add_item(student)
        self._operations.append(AddOperation(student))
        self._index += 1
        self.controller_undo_redo.add([self])

    def remove_student(self, student_id):
        """
        Removes a student from the list of students

        :param student_id: positive integer
        :return:
        """
        stud = self.get_by_id(student_id)
        self._repository.remove_item(student_id)
        self._operations.append(RemoveOperation(stud))
        self._index += 1
        self.controller_undo_redo.add([self])

    def update_student(self, student_id, name, group):
        """
        Finds the student with the same id and changes his/her name and/or group

        :param student_id: positive integer
        :param name: syring
        :param group: positive integer
        :return:
        """
        old_student = deepcopy(self._repository.get_by_id(student_id))
        student = Student(student_id, name, group)
        self._validator.validate_student(student)
        self._repository.update_item(student)
        new_stud = self.get_by_id(student_id)
        self._operations.append(UpdateOperation(old_student, new_stud))
        self._index += 1
        self.controller_undo_redo.add([self])

    def get_by_id(self, stud_id):
        """
        Finds the student with the id given
        """
        return self._repository.get_by_id(stud_id)

    def read(self):
        self._repository.reading()

    def write(self):
        self._repository.writing()

    def undo(self):
        """
        Undo the last student operation that changed the set of students
        Returns True if operation was undone, False otherwise
        """
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
