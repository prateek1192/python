__author__ = 'Prateek'

def strdecor(func):
    def add_decor(*args,**kwargs):
        return "[{}]".format(func(args[0]))

    return add_decor
@strdecor
def demo(value):
    return value

print demo('peter pan')