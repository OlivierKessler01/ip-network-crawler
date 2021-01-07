import unittest

class TestConcretion:
    def __init__(self):
        pass

class Factory:
    '''
        Base class for factories
        Use composition over inheritance when possible
    '''
    classes_to_instanciate = {"test" : TestConcretion}

    def get(self, classname):
        try:
            object_to_return = (self.classes_to_instanciate[classname])()
            return object_to_return
        except KeyError:
            print("No class found for index", classname)


class FactoryTest(unittest.TestCase):
    def test_instantiation(self):
        factory = Factory()
        concretion = factory.get("test")
        self.assertIsInstance(concretion, TestConcretion)

if __name__ == "__main__":
    unittest.main()
