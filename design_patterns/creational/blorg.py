class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        pass


""" USAGE:
print(Borg())
print(Borg())
"""
