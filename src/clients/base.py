import subprocess

def run(args):
    r = subprocess.run(args, stdout=subprocess.PIPE)
    return r.stdout.decode("utf-8")

def to_object(dict):
    return dict_class(dict)

class dict_class:
    def __init__(self, data):
        self.__dict__ = data
