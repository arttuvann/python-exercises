#test suite
import unittest


from hello_world import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_output(self):
        actual = hello_world()
        expected = "Hello world!"
        self.assertEqual(actual, expected)