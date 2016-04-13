'''
Created on Nov 16, 2015

@author: AndiD
'''

from exceptions.Exceptions import CustomException
from operator import itemgetter

class Console:
    def __init__(self, contr):
        """
        Creates a new object of type console
        """
        self.contr = contr

    def ui_add_student(self):
        student_id = int(input("student_id = "))
        name = input("name = ")
        group = int(input("group = "))
        try:
            self.contr.add_student(student_id, name, group)
        except CustomException as e:
            print(e.get_msg())

    def ui_add_assignment(self):
        assign_id = int(input("assignment_id = "))
        student_id = int(input("student_id = "))
        description = input("description = ")
        deadline = input("deadline = ")
        grade = int(input("grade = "))
        try:
            self.contr.add_assignment(assign_id, student_id, description, deadline, grade)
        except CustomException as e:
            print(e.get_msg())

    def ui_get_student(self):
        student_id = int(input("student_id = "))
        try:
            print(self.contr.get_student_by_id(student_id))
        except CustomException as e:
            print(e.get_msg())

    def ui_get_students_on_assign(self):
        assign_id = int(input("assignment_id = "))
        try:
            result = self.contr.get_students_on_assignment_by_id(assign_id)
        except CustomException as e:
            print(e.get_msg())
        return result

    def ui_update_student(self):
        student_id = int(input("student_id = "))
        name = input("name = ")
        group = int(input("group = "))
        try:
            self.contr.update_student(student_id, name, group)
        except CustomException as e:
            print(e.get_msg())

    def ui_update_assignment(self):
        assign_id = int(input("assignment_id = "))
        student_id = int(input("student_id = "))
        description = input("description = ")
        deadline = input("deadline = ")
        grade = int(input("grade = "))
        try:
            self.contr.update_assignment(assign_id, student_id, description, deadline, grade)
        except CustomException as e:
            print(e.get_msg())

    def ui_remove_student(self):
        student_id = int(input("student_id = "))
        try:
            self.contr.remove_student(student_id)
        except CustomException as e:
            print(e.get_msg())

    def ui_remove_assignment(self):
        assign_id = int(input("assignment_id = "))
        try:
            self.contr.remove_assignment(assign_id)
        except CustomException as e:
            print(e.get_msg())

    def ui_print_students(self):
        for st in self.contr.get_all_students():
            print(st)

    def ui_print_assignments(self):
        for assign in self.contr.get_all_assignments():
            print(assign)

    def ui_get_student_sorted_alphabetically(self):
        list_students_grades_on_assign = self.ui_get_students_on_assign()
        my_list = sorted(list_students_grades_on_assign, key=itemgetter(0))
        print(my_list)

    def ui_students_grade_lower_5(self):
        list_students_grades = self.ui_get_students_on_assign()
        my_list = []
        for i in list_students_grades:
            if i[1] <= 5:
                my_list.append(i)
        my_list = sorted(my_list, key=itemgetter(1))
        print(my_list)

    def ui_undo_students(self):
        try:
            self.contr.undo_last_mod_student()
        except CustomException as e:
            print(e.get_msg())

    def ui_undo_assign(self):
        try:
            self.contr.undo_last_mod_assign()
        except CustomException as e:
            print(e.get_msg())

    def ui_redo_students(self):
        try:
            self.contr.redo_last_mod_student()
        except CustomException as e:
            print(e.get_msg())

    def ui_redo_assign(self):
        try:
            self.contr.redo_last_mod_assign()
        except CustomException as e:
            print(e.get_msg())

    def show_main_menu(self):
        print("\n\
            Please choose one option\n\
            1 - add student\n\
            2 - add an assignment\n\
            3 - get student by id \n\
            4 - get all students at assignment ordered alphabetically\n\
            5 - update student \n\
            6 - update assignment \n\
            7 - remove student \n\
            8 - remove assignment \n\
            9 - show all students with grade less than 5 (ordered) \n\
            10 - print students \n\
            11 - print assignments \n\
            12 - undo last modification in the list of students \n\
            13 - undo last modification in the list of assignments \n\
            14 - redo modifications in the list of students \n\
            15 - redo modifications in the list of assignments \n\
            0 - exit \n\
            ")

    def example(self):
        print("hello")

    def run(self):
        options = {1: self.ui_add_student, 2: self.ui_add_assignment, 3: self.ui_get_student,
                   4: self.ui_get_student_sorted_alphabetically, 5: self.ui_update_student, 6: self.ui_update_assignment,
                   7: self.ui_remove_student, 8: self.ui_remove_assignment, 9: self.ui_students_grade_lower_5,
                   10: self.ui_print_students, 11: self.ui_print_assignments, 12: self.ui_undo_students,
                   13: self.ui_undo_assign, 14: self.ui_redo_students, 15: self.ui_redo_assign}
        while True:
            self.show_main_menu()
            opt = input("option = ")
            if opt == "0":
                break
            try:
                opt = int(opt)
                options[opt]()
            except ValueError:
                print("This input is not valid")
            except KeyError:
                print("Option is not implemented")

