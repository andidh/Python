__author__ = 'ecaterinacarazan'


class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def get_msg(self):
        return self.msg
