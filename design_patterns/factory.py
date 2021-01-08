import sys

class Factory:
    '''
        Base class for factories
        Use composition over inheritance when possible
    '''
    classes_to_instanciate = {}

    def __init__(self, classes_to_instanciate: dict[str, str]):
        self.classes_to_instanciate = classes_to_instanciate

    def get(self, classname:str, out=sys.stdout):
        '''
            classname : the class to instanciate
            out : output to print the errors to
        '''

        try:
            object_to_return = (self.classes_to_instanciate[classname])()
            return object_to_return
        except KeyError:
            out.write("No class found for index " + classname)
