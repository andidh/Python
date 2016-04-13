'''
Created on Nov 16, 2015

@author: AndiD
'''
from contr.ControllerException import ControllerException
from domain.Assignment import Assignment
from domain.Student import Student


class Controller:

    def __init__(self, repository, validator):
        """
        Creates a new instance of controller
        :param repository: the repository for data
        :param validator: the class to validate the input data
        :return:
        """
        self._repository = repository
        self._validator = validator

    def get_repository(self):
        return self._repository

    def get_all_students(self):
        return self._repository.get_list_of_students()

    def get_all_assignments(self):
        return self._repository.get_list_of_assignments()

    def add_assignment(self, id_assign, student_id, description, deadline, grade):
        """
        Adds an assignment to the list of assignments

        :param id_assign: positive integer
        :param student_id: positive integer
        :param description: string
        :param deadline: string
        :param grade: positive integer < 10
        :return:
        """
        assign = Assignment(id_assign, student_id, description, deadline, grade)
        self._validator.validate_assignment(assign)
        # for assign in self._repository.get_list_of_assignments():
        #     if assign.get_assignment_id() == id_assign:
        #         raise ControllerException("Can not add assignment with same id")
        self._repository.add_assignment(assign)

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
        for stud in self._repository.get_list_of_students():
            if stud.get_student_id() == student_id:
                raise ControllerException("Can not add student with same id")
        self._repository.add_student(student)

    def remove_student(self, student_id):
        """
        Removes a student from the list of students

        :param student_id: positive integer
        :return:
        """
        self._repository.remove_student(student_id)

    def remove_assignment(self, assign_id):
        """
        Removes an assignment from the list of assignments

        :param assign_id: positive integer
        :return:
        """
        self._repository.remove_assignment(assign_id)

    def update_student(self, student_id, name, group):
        """
        Finds the student with the same id and changes his/her name and/or group

        :param student_id: positive integer
        :param name: syring
        :param group: positive integer
        :return:
        """
        student = Student(student_id, name, group)
        self._validator.validate_student(student)
        self._repository.update_student(student)

    def update_assignment(self, id_assign, student_id, description, deadline, grade):
        """
        Finds the assignment with the same id and changes the rest of the fields with the new values

        :param id_assign: positive integer
        :param student_id: positive integer
        :param description: string
        :param deadline: string
        :param grade: positive integer < 10
        :return:
        """
        assign = Assignment(id_assign, student_id, description, deadline, grade)
        self._validator.validate_assignment(assign)
        self._repository.update_assignment(assign)

    def get_student_by_id(self, id):
        """
        Finds a student with the id given

        :param id: positive integer
        :return:
        """
        return self._repository.get_student_by_id(id)

    def get_students_on_assignment_by_id(self, id):
        """
        Finds the students subscribed on the same course and shows their grade as well

        :param id: positive integer
        :return:
        """
        return self._repository.get_students_on_assignment_by_id(id)

    def undo_last_mod_student(self):
        """
        Undoes the last modification made on list of students

        backup_list is a list of all states of the list of students
        when undo, takes the last state from backup list and assigns the list of students to it.
        also delete the last state from backup list.
        :return:
        """
        if len(self._repository.get_backup_list_stud()) == 0:
            raise ControllerException("You can't undo the first operation")
        back = self._repository.get_backup_list_stud()
        self._repository.add_to_redo_stud_list(self._repository.get_list_of_students())
        self._repository.set_list_of_students(back[-1])
        del back[-1]
        self._repository.set_backup_list_stud(back)

    def undo_last_mod_assign(self):
        """
        Undoes the last modification made on list of assignments

        backup_list is a list of all states of the list of assignments
        when undo, takes the last state from backup list and assigns the list of assignments to it.
        also delete the last state from backup list.
        :return:
        """
        if len(self._repository.get_backup_list_assign()) == 0:
            raise ControllerException("You can't undo the first operation")
        self._repository.add_to_redo_assign_list(self._repository.get_list_of_assignments())
        back = self._repository.get_backup_list_assign()
        self._repository.set_list_of_assignments(back[-1])
        del back[-1]
        self._repository.set_backup_list_assign(back)

    def redo_last_mod_student(self):
        """
        redo the last modification made by undo (on list of students)

        redo list is a list of all the states which were  undone
        when redo, take the last state and assign it to list of students,
        extend the backup list again

        :return:
        """
        print(len(self._repository.get_redo_stud_list()))
        if len(self._repository.get_redo_stud_list()) == 0:
            raise ControllerException("You can't undo the first operation")
        red_list = self._repository.get_backup_list_stud() + [self._repository.get_list_of_students()]
        self._repository.set_backup_list_stud(red_list)
        self._repository.set_list_of_students(self._repository.get_redo_stud_list()[-1])
        self._repository.remove_from_redo_stud_list()

    def redo_last_mod_assign(self):
        """
        redo the last modification made by undo (on list of assignments

        redo list is a list of all the states which were undone
        when redo, take the last state and assign it to list of assignments,
        extend the backup list again
        :return:
        """
        print(len(self._repository.get_redo_assign_list()))
        if len(self._repository.get_redo_assign_list()) == 0:
            raise ControllerException("You can't redo the first operation")
        red_list = self._repository.get_backup_list_assign() + [self._repository.get_list_of_assignments()]
        self._repository.set_backup_list_assign(red_list)
        self._repository.set_list_of_assignments(self._repository.get_redo_assign_list()[-1])
        self._repository.remove_from_redo_assign_list()

