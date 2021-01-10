import sys

class Factory:
    '''
        Base class for factories
        Use composition over inheritance when possible
    '''

    def __init__(self, classes_to_instanciate : dict[str, str] = {}):
        self.classes_to_instanciate = classes_to_instanciate
        self.last_requested = None

    def get_last(self):
        return self.last_requested

    def get(self, classname:str, out=sys.stdout):
        '''
            classname : the class to instanciate
            out : output to print the errors to
        '''

        try:
            self.last_requested = (self.classes_to_instanciate[classname])()
            return self.last_requested
        except KeyError:
            out.write("No class found for index " + classname)
