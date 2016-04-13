from exc.MyException import CustomException


class Console:
    def __init__(self, contr_student, contr_assign, contr_grade, controller_undo_redo):
        self.controller_student = contr_student
        self.controller_assign = contr_assign
        self.controller_grade = contr_grade
        self.controller_undo_redo = controller_undo_redo

    def ui_add_student(self):
        student_id = int(input("student_id = "))
        name = input("name = ")
        group = int(input("group = "))
        try:
            self.controller_student.add_student(student_id, name, group)
        except CustomException as e:
            print(e.get_msg())

    def ui_add_assignment(self):
        assign_id = int(input("assignment_id = "))
        description = input("description = ")
        deadline = input("deadline = ")
        try:
            self.controller_assign.add_assignment(assign_id, description, deadline)
        except CustomException as e:
            print(e.get_msg())

    def ui_update_student(self):
        student_id = int(input("student_id = "))
        name = input("name = ")
        group = int(input("group = "))
        try:
            self.controller_student.update_student(student_id, name, group)
        except CustomException as e:
            print(e.get_msg())

    def ui_update_assignment(self):
        assign_id = int(input("assignment_id = "))
        description = input("description = ")
        deadline = input("deadline = ")
        try:
            self.controller_assign.update_assignment(assign_id, description, deadline)
        except CustomException as e:
            print(e.get_msg())

    def ui_remove_student(self):
        student_id = int(input("student_id = "))
        try:
            self.controller_student.remove_student(student_id)
        except CustomException as e:
            print(e.get_msg())
        for grade in self.controller_grade.get_all_grades():
            if grade.get_student().get_id() == student_id:
                self.controller_grade.remove_grade(grade.get_id())

    def ui_remove_assignment(self):
        assign_id = int(input("assignment_id = "))
        try:
            self.controller_assign.remove_assignment(assign_id)
        except CustomException as e:
            print(e.get_msg())
        for grade in self.controller_grade.get_all_grades():
            if grade.get_assignment().get_id() == assign_id:
                self.controller_grade.remove_grade(grade.get_id())

    def ui_print_students(self):
        for st in self.controller_student.get_all_students():
            print(st)

    def ui_print_assignments(self):
        for assign in self.controller_assign.get_all_assignments():
            print(assign)

    def get_student_by_id(self):
        id = int(input("give id"))
        print(self.controller_student.get_by_id(id))

    def ui_add_a_grade(self):
        student_id = int(input("Give student id:"))
        assignment_id = int(input("Give assignment id:"))
        grade_id = int(input("Give grade id:"))
        grade = int(input("Grade = "))
        try:
            self.controller_grade.add_grade(student_id, assignment_id, grade_id, grade)
        except CustomException as e:
            print(e.get_msg())

    def print_grades(self):
        for grade in self.controller_grade.get_all_grades():
            print(grade)
            print(" ")

    def ui_remove_grade(self):
        grade_id = int(input("give grade id = "))
        try:
            self.controller_grade.remove_grade(grade_id)
        except CustomException as e:
            print(e.get_msg())

    def ui_update_grade(self):
        grade_id = int(input("give grade id = "))
        grade = int(input("give grade = "))
        try:
            self.controller_grade.update_grade(grade_id, grade)
        except CustomException as e:
            print(e.get_msg())

    def students_grades_one_assign(self):
        assign_id = int(input("give asignment id = "))
        my_list = self.controller_grade.order_alphabetically(assign_id)
        print(my_list)

    def student_grades_lower_5(self):
        assign_id = int(input("give asignment id = "))
        my_list = self.controller_grade.order_by_grade_lower_5(assign_id)
        print(my_list)

    def undo(self):
        try:
            self.controller_undo_redo.undo()
        except CustomException as e:
            print(e.get_msg())

    def redo(self):
        try:
            self.controller_undo_redo.redo()
        except CustomException as e:
            print(e.get_msg())

    def read_file(self):
        try:
            self.controller_student.read()
            self.controller_assign.read()
            self.controller_grade.read()
            self.run("yes")
        except CustomException as e:
            print(e.get_msg())

    def write_file(self):
        self.controller_student.write()
        self.controller_assign.write()
        self.controller_grade.write()

    def show_main_menu(self):
        print('\n\
            Please choose one option\n\
            1 - add student\n\
            2 - add an assignment\n\
            3 - update student \n\
            4 - update assignment \n\
            5 - remove student \n\
            6 - remove assignment \n\
            7 - print students \n\
            8 - print assignments \n\
            9 - add a grade \n\
            10 - print all grades \n\
            11 - print student by id \n\
            12 - remove grade \n\
            13 - update grade \n\
            14 - get students ordered alphabetically and their grades on one assignment \n\
            15 - get all students with grade <5 at one assignment \n\
            16 - undo last modification \n\
            17 - redo last modification \n\
            18 - read from file \n\
            19 - write to file \n\
            0 - exit \n\
            ')

    def run(self, string):
        options = {1: self.ui_add_student, 2: self.ui_add_assignment, 3: self.ui_update_student,
                   4: self.ui_update_assignment, 5: self.ui_remove_student, 6: self.ui_remove_assignment,
                   7: self.ui_print_students, 8: self.ui_print_assignments, 9: self.ui_add_a_grade,
                   10: self.print_grades, 11: self.get_student_by_id, 12: self.ui_remove_grade, 13: self.ui_update_grade,
                   14: self.students_grades_one_assign, 15: self.student_grades_lower_5, 16: self.undo, 17: self.redo,
                   18: self.read_file, 19: self.write_file}
        while True:
            self.show_main_menu()
            opt = input("option = ")
            if opt == "0":
                if string == "yes":
                    self.write_file()
                exit(0)
            try:
                opt = int(opt)
                options[opt]()
            except ValueError:
                print("This input is not valid")
            except KeyError:
                print("Option is not implemented")

    def pre_run(self):
        result = int(input("Press 1 for memory storage or 2 for in-file storage:"))
        storage = {1: self.run, 2: self.read_file}
        while True:
            try:
                if result == 1:
                    storage[1]("no")
                elif result == 2:
                    storage[2]()
            except ValueError:
                print("This input is not valid")
            except KeyError:
                print("Option is not implemented")