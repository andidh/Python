'''
Created on Dec 14, 2015

@author: AndiD
'''
from contr.ControllerException import ControllerException
from domain.Student import Student
from repository.Repository import Repository


class RepoWritingFileStudent(Repository):
    def __init__(self):
        Repository.__init__(self)

    def reading(self):
        file = open("/Users/AndiD//Documents/Eclipse/lab57/student.txt", "r")
        lines = file.read().splitlines()
        for line in lines:
            list = line.split(", ")
            stud = Student(int(list[0]), list[1], int(list[2]))
            for s in Repository.get_all(self):
                if s.get_id() == int(list[0]):
                    raise ControllerException("Can not add student with same id")
            Repository.add_item(self, stud)
        file.close()

    def writing(self):
        file = open("/Users/AndiD//Documents/Eclipse/lab57/student.txt", "w")
        list = Repository.get_all(self)
        for stud in list:
            string = str(stud.get_id()) + ", " + str(stud.get_name()) + ", " + str(stud.get_group())
            file.write(string + "\n")
        file.close()
