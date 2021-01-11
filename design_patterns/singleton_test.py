import unittest
from singleton import Singleton

class SingletonTest(unittest.TestCase):
    def test_get_instance(self):
        instance = Singleton.get_instance()
        self.assertIsInstance(instance, Singleton)
        instance2 = Singleton.get_instance()
        self.assertEqual(instance, instance2)

if __name__ == "__main__":
    unittest.main()
