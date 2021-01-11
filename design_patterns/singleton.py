import importlib

class Singleton:
    '''
        The Singleton design pattern is a creational design pattern. It ensures a class only has one instance
        and provides a global point of access to it.

        Inherits this class and override the class and module attributes to use it
    '''
    instance = None
    #override this
    classname_of_object = "Singleton"
    module_of_class = "singleton"

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            module = importlib.import_module(cls.module_of_class)
            cls.instance = getattr(module, cls.classname_of_object)()
        return cls.instance
