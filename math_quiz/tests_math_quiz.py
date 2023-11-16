import unittest
from math_quiz import num_generator, operation_selection, math_operation
class TestMathGame(unittest.TestCase):
    def test_function_num_gen(self):
        # Test if random numbers generated are within the specified range

        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = num_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
    def test_function_operation_selection(self):
        # Test if operation selection is right

        operators_list = ['+', '-', '*']
        for _ in range(1000):
            selected_operator = operation_selection()
            self.assertIn(selected_operator, operators_list)
    def test_function_math_operation(self):
        # Test the math operation function
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (18, 9, '-', '18 - 9', 9),
            (3, 5, '*', '3 * 5', 15),
            (4, 9, '+', '4 + 9', 13),
            (15, 12, '-', '15 - 12', 3),
            (4, 7, '*', '4 * 7', 28),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = math_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()

