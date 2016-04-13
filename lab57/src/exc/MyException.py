'''
Created on Dec 14, 2015

@author: AndiD
'''

class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def get_msg(self):
        return self.msg
