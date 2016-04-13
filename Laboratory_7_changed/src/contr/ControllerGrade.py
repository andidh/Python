from operator import itemgetter
from contr.ControllerException import ControllerException
from contr.UndoableOperations import AddOperation, RemoveOperation, UpdateOperation
from domain.Grade import Grade


class ControllerGrade:
    def __init__(self, repository_student, repository_assign, repo, validator, controller_undo_redo):
        """
        initialise the main controller with the fields: controllers for student and assign, repository and validator for grade, undo_redo_repository
        """
        self.__repo_stud = repository_student
        self.__repo_assign = repository_assign
        self.__repository = repo
        self.__validator = validator
        self.controller_undo_redo = controller_undo_redo
        self._operations = []
        self._index = 0

    def add_grade(self, student_id, assign_id, grade_id, grade):
        """
        adds a grade
        :param student_id: > 0
        :param assign_id: > 0
        :param grade_id: > 0
        :param grade: between 0 and 10
        :return:
        """
        student = self.__repo_stud.get_by_id(student_id)
        assign = self.__repo_assign.get_by_id(assign_id)
        grade = Grade(grade_id, student, assign, grade)
        self.__validator.validate_grade(grade)
        for g in self.__repository.get_all():
            if g.get_id() == grade_id:
                raise ControllerException("Can not add grade with same id")
        self.__repository.add_item(grade)
        self._operations.append(AddOperation(grade))
        self._index += 1
        self.controller_undo_redo.add([self])

    def get_all_grades(self):
        """
        returns all grades
        :return:
        """
        return self.__repository.get_all()

    def get_by_id(self, id_grade):
        return self.__repository.get_by_id(id_grade)

    def remove_grade(self, grade_id):
        """
        removes a grade
        :param grade_id: > 0
        :return:
        """
        grade = self.get_by_id(grade_id)
        self.__repository.remove_item(grade_id)
        self._operations.append(RemoveOperation(grade))
        self._index += 1
        self.controller_undo_redo.add([self])


    def update_grade(self, grade_id, grade):
        """
        updates a grade
        :param grade_id: > 0
        :param grade:  between 0 and 10
        :return:
        """
        g = self.__repository.get_by_id(grade_id)
        gr = Grade(g.get_id(), g.get_student(), g.get_assignment(), grade)
        self.__validator.validate_grade(gr)
        self.__repository.update_item(gr)
        new_grade = self.get_by_id(grade_id)
        self._operations.append(UpdateOperation(g, new_grade))
        self._index += 1
        self.controller_undo_redo.add([self])

    def stud_grade_one_assign(self, assign_id):
        """
        returns all students and their grades at one single assignment
        :param assign_id:
        :return:
        """
        list_of_students = []
        for grade in self.get_all_grades():
            if grade.get_assignment().get_id() == assign_id:
                list_of_students.append([grade.get_student().get_name(), grade.get_grade()])
        return list_of_students

    def order_alphabetically(self, assign_id):
        """
        orders alphabetically the list of students and their grades
        :param assign_id: > 0
        :return:
        """
        list_of_stud = self.stud_grade_one_assign(assign_id)
        my_list = sorted(list_of_stud, key=itemgetter(0))
        return my_list

    def order_by_grade_lower_5(self, assign_id):
        """
        orders by their grade (<5) the list of students and their grades
        :param assign_id: > 0
        :return:
        """
        list_of_stud = self.stud_grade_one_assign(assign_id)
        my_list = []
        for i in list_of_stud:
            if i[1] <= 5:
                my_list.append(i)
        my_list = sorted(my_list, key=itemgetter(1))
        return my_list

    def read(self):
        self.__repository.reading()

    def write(self):
        self.__repository.writing()

    def undo(self):
        if self._index == 0:
            return False

        self._index -= 1
        operation = self._operations[self._index]

        if isinstance(operation, AddOperation):
            self.__repository.remove_item(operation.get_item().get_id())
        elif isinstance(operation, RemoveOperation):
            self.__repository.add_item(operation.get_item())
        elif isinstance(operation, UpdateOperation):
            self.__repository.update_item(operation.get_old())
        else:
            self._index +=1

    def redo(self):
        if self._index >= len(self._operations):
            return False

        operation = self._operations[self._index]
        if isinstance(operation, AddOperation):
            self.__repository.add_item(operation.get_item())
            self._index +=1
        elif isinstance(operation, RemoveOperation):
            self.__repository.remove_item(operation.get_item().get_id())
            self._index +=1
        elif isinstance(operation, UpdateOperation):
            self.__repository.update_item(operation.get_updated())
            self._index +=1
        else:
            self._index -= 1


