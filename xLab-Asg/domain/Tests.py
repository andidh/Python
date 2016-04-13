'''
Created on Dec 21, 2015

@author: AndiD
'''
from domain.Entities import Student, Lab
from domain.Validator import *

def testStudent():
    s = Student(1, "Andrei")
    assert s.get_id() == 1
    assert s.get_name() == "Andrei"
    s = Student(-1, "Alex")
    val = StudentValidator()
    try:
        val.validate(s)
        print(False)
    except CustomException:
        print(True)
    
    
testStudent()