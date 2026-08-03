import unittest
import exercise

class TestGame(unittest.TestCase): 
    def test_input(self):
        answer = 5
        guess = 5 
        result = exercise.run_guess(guess, answer)   # we call the function run_guess from exercise.py with the guess and answer as input
        self.assertTrue(result)

    def test_input_wrong_guess(self): 
        result = exercise.run_guess(0, 5)
        self.assertFalse(result)

    def test_input_wrong_number(self): 
        result = exercise.run_guess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_input(self): 
        result = exercise.run_guess(5, '11')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()