'''
Created on Nov 16, 2015

@author: AndiD
'''
from copy import deepcopy

from repos.RepositoryException import *


class Repository:
    def __init__(self):
        self._list_of_students = []
        self._list_of_assignments = []
        self._backup_list_stud = []
        self._backup_list_assign = []
        self._redo_stud_list = []
        self._redo_assign_list = []

    def add_to_redo_assign_list(self, redo_list):
        self._redo_assign_list.append(redo_list)

    def get_redo_assign_list(self):
        return self._redo_assign_list

    def remove_from_redo_assign_list(self):
        """
        remove the last element from the redo_assign_list

        :return:
        """
        del self._redo_assign_list[-1]

    def add_to_redo_stud_list(self, redo_list):
        self._redo_stud_list.append(redo_list)

    def get_redo_stud_list(self):
        return self._redo_stud_list

    def remove_from_redo_stud_list(self):
        """
        remove the last element from the redo_stud_list

        :return:
        """
        del self._redo_stud_list[-1]

    def get_list_of_students(self):
        return self._list_of_students

    def get_list_of_assignments(self):
        return self._list_of_assignments

    def set_list_of_students(self, list_of_students):
        self._list_of_students = list_of_students

    def set_list_of_assignments(self, list_of_assignments):
        self._list_of_assignments = list_of_assignments

    def get_backup_list_stud(self):
        return self._backup_list_stud

    def set_backup_list_stud(self, backup_list_stud):
        self._backup_list_stud = backup_list_stud

    def set_backup_list_assign(self, backup_list_assign):
        self._backup_list_assign = backup_list_assign

    def get_backup_list_assign(self):
        return self._backup_list_assign

    def get_student_by_id(self, id):
        """
        Finds the student with the id given

        :param id: positive integer
        :return:
        """
        index = -1
        for i in range(len(self._list_of_students)):
            if self._list_of_students[i].get_student_id() == id:
                index = i
                break
        if index == -1:
            raise RepositoryException("No student with such id")
        else:
            return self._list_of_students[index]

    def get_students_on_assignment_by_id(self, id):
        """
        Finds all students subscribed on the assignment given and their grades

        :param id: positive integer
        :return:
        """
        list_of_students_on_assign = []
        for i in range(len(self._list_of_assignments)):
            if self._list_of_assignments[i].get_assignment_id() == id:
                list_of_students_on_assign.append([self.get_student_by_id(self._list_of_assignments[i].get_student_id()).get_name(), self._list_of_assignments[i].get_grade()])
        return list_of_students_on_assign

    def add_student(self, stud):
        """
        Adds a student to the list

        :param stud: object of type Student
        :return:
        """
        self._backup_list_stud.append(deepcopy(self._list_of_students))
        self._list_of_students.append(stud)

    def add_assignment(self, assign):
        """
        Adds an asignment to the list

        :param assign: object of type Assignment
        :return:
        """
        self._backup_list_assign.append(deepcopy(self._list_of_assignments))
        self._list_of_assignments.append(assign)

    def remove_student(self, student_id):
        """
        Removes a student from the list by the given id

        :param student_id: positive integer
        :return:
        """
        for student in self._list_of_students:
            if student.get_student_id() == student_id:
                self._backup_list_stud.append(deepcopy(self._list_of_students))
                self._list_of_students.remove(student)
                return
        raise RepositoryException("No such student")

    def remove_assignment(self, assign_id):
        """
        Removes an assignment from the list by given id

        :param assign_id: positive integer
        :return:
        """
        for assign in self._list_of_assignments:
            if assign.get_assignment_id() == assign_id:
                self._backup_list_assign.append(deepcopy(self._list_of_assignments))
                self._list_of_assignments.remove(assign)
                return
        raise RepositoryException("No such assignment")

    def update_student(self, student):
        """
        Finds the student with the same id and updates the rest of fields with new values

        :param student: object of type Student
        :return:
        """
        index = -1
        for i in range(len(self._list_of_students)):
            if self._list_of_students[i].get_student_id() == student.get_student_id():
                index = i
                break
        if index == -1:
            raise RepositoryException("No student for update found")
        else:
            self._backup_list_stud.append(deepcopy(self._list_of_students))
            self._list_of_students[index] = student

    def update_assignment(self, assign):
        """
        Finds the assignment with the same id and updates the rest of fields with the new values

        :param assign: object of type Assignment
        :return:
        """
        index = -1
        for i in range(len(self._list_of_assignments)):
            if self._list_of_assignments[i].get_assignment_id() == assign.get_assignment_id():
                index = i
                break
        if index == -1:
            raise RepositoryException("No assignment for update found")
        else:
            self._backup_list_assign.append(deepcopy(self._list_of_assignments))
            self._list_of_assignments[index] = assign


