
'''
Created on Dec 14, 2015

@author: AndiD
'''
from console.Console import Console
from contr.ControllerAssign import ControllerAssignment
from contr.ControllerGrade import ControllerGrade
from contr.ControllerStudent import ControllerStudent
from contr.ControllerUndoRedo import UndoController
from contr.ValidatorAssignment import ValidatorAssign
from contr.ValidatorGrade import ValidatorGrade
from contr.ValidatorStudent import ValidatorStudent
from repository.RepoWritingFileAssign import RepoWritingFileAssign
from repository.RepoWritingFileGrade import RepoWritingFileGrade
from repository.RepoWritingFileStudent import RepoWritingFileStudent


def main():
    student_repo = RepoWritingFileStudent()
    assign_repo = RepoWritingFileAssign()
    grade_repo = RepoWritingFileGrade(student_repo, assign_repo)
    validator_student = ValidatorStudent()
    validator_assign = ValidatorAssign()
    validator_grade = ValidatorGrade()
    controller_undo_redo = UndoController()
    controller_student = ControllerStudent(student_repo, validator_student, controller_undo_redo)
    controller_assignment = ControllerAssignment(assign_repo, validator_assign, controller_undo_redo)
    controller_grade = ControllerGrade(student_repo, assign_repo, grade_repo, validator_grade, controller_undo_redo)
    console = Console(controller_student, controller_assignment, controller_grade, controller_undo_redo)
    console.pre_run()


main()
