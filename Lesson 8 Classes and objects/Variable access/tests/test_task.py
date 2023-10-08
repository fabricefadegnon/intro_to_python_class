import contextlib
import io
import unittest
import re

try:
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        from access_variable import MyClass, my_object, another_object
    output = f.getvalue().split('\n')


    class TestCase(unittest.TestCase):
        def test_instances(self):
            self.assertTrue(isinstance(my_object, MyClass), msg='The object my_object has to be an instance of MyClass.')
            self.assertTrue(isinstance(another_object, MyClass), msg='The object another_object has to be an instance of MyClass.')

        def test_out(self):
            expected, actual = str(my_object.variable1), output[2]
            self.assertEqual(expected, actual, msg='Your code should print the value of the '
                                                                'variable1 attribute of my_object in the third'
                                                                      'print statement.')

        def test_method_call_syntax(self):
            self.assertFalse('<bound method ' in output[3], msg='To call a method properly, you need to use the syntax such as `object.method()`. '
                                                                'Without brackets, this will just return the function object.')


except ImportError:
    class TestFailCase(unittest.TestCase):
        def test_fail(self):
            self.assertTrue(False, msg='Please do not change class and variable names.')



