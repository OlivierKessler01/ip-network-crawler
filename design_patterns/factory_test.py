from io import StringIO
import unittest
from factory import Factory

class TestConcretion:
        def __init__(self):
            pass

class FactoryTest(unittest.TestCase):

    def test_get_success(self):
        factory = Factory({"test" : TestConcretion})
        concretion = factory.get("test", StringIO())
        self.assertIsInstance(concretion, TestConcretion)

    def test_get_error(self):
        '''
            Make sure we handle the case where the demanded class doesn't exist
        '''
        out = StringIO()
        factory = Factory({"test" : TestConcretion})
                
        try:
            factory.get("tt", out)
        except KeyError:
            self.fail("get() raised KeyError unexpectedly")

        self.assertEqual(out.getvalue().strip(), "No class found for index tt")


if __name__ == "__main__":
    unittest.main()



