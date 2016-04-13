'''
Created on Nov 16, 2015

@author: AndiD
'''


class CustomException(Exception):
    def __init__(self, msg):
        """
        inherit from exception
        :param msg:
        :return:
        """
        self.msg = msg

    def get_msg(self):
        return self.msg
