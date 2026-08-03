import unittest 
import main # we use all the functions from main.py

class TestMain(unittest.TestCase): # standard way to create a test class, we inherit from unittest.TestCase
    def setUp(self): # this function is called before each test, we can use it to set up any variables we need for the tests
        print('about to test a function')

    def test_do_stuff(self): 
        test_param = 10
        result = main.do_stuff(test_param)   # we call the function do_stuff from main.py with the test_param as input
        self.assertEqual(result,15) # we expect 10 + 5 = 15, so we check if the result is equal to 15


    def test_do_stuff2(self): 
            test_param = 'asdsadsa'
            result = main.do_stuff(test_param)   # we call the function do_stuff from main.py with the test_param as input
            self.assertIsInstance(result, ValueError) # we expect a ValueError to be raised, so we check if the result is an instance of ValueError


    def test_do_stuff3(self):
         test_param = None 
         result = main.do_stuff(test_param)   # we call the function do_stuff from main.py with the test_param as input
         self.assertEqual(result, 'please enter number')
         
if __name__ == '__main__':
    unittest.main()