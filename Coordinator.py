import random


class Coordinator:
    def __init__(self):
        self.__hash = random.getrandbits(128)

    def proccess_request(self, action, args):
        if self.__hash == "":
            return None
        else:
            action(args)
            return self.__hash

    def set_hash(self, value):
        self.__hash = value

    def get_hash(self):
        return self.__hash
