# akerl, 2013
# https://github.com/akerl/modlib

'''modlib maintains a stack of dynamically-loaded module objects
useful when you need to import dynamic modules with some degree of control
'''

from os.path import isfile, expanduser
from importlib import import_module

class Modstack(object):
    '''formula is used by other methods to determine path of module
        it is a .format-able string accepting keyword arguments
    target is the thing to import from the module
        use None to import the full module
    cleanify controls if Modstack accepts "pythonic" module paths
        if True: "." is converted to "/" and ".py" is appended
        if False: No changes are made to the formula string
    '''
    def __init__(self,
                 formula='{0}',
                 target=None,
                 cleanify=True):
        self.stack = {}
        self.target = target
        if cleanify:
            self.formula = formula.replace('.', '/') + '.py'
        else:
            self.formula = formula
    '''args and kwargs are used for compilation
    '''
    def compile_path(self, *args, **kwargs):
        path = self.formula.format(*args, **kwargs)
        path = expanduser(path)
        return path
    '''args and kwargs go straight to compile_path
    you ask for a match, you get back a thing
    '''
    def get(self, *args, **kwargs):
        path = self.compile_path(*args, **kwargs)
        if path in self.stack:
            return self.stack[path]
        else:
            if self.target is None:
                new_object = import_module(path)
            else:
                new_object = getattr(import_module(path), self.target)
            self.stack.update({path: new_object})
            return new_object
 
