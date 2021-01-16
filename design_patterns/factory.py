import sys

class InstantiationError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class Factory:
    '''
        The Factory method design pattern is a creational pattern, it allows a class to defer instanciation to the factory, thus doesn't need to bother with the complexity of object instantiation
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
            raise InstantiationError("get", "No class found for index ")
