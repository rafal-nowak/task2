from pathlib import Path
import sys

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

import unittest

from src.task import equal_strings
from test.test_logger import TestLogger


class TaskTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = TestLogger()

    @classmethod
    def tearDownClass(cls):
        cls.logger.save_results()

    def test_should_compare_two_identical_strings(self):
        s1 = "konstantynopolitaneczka"
        s2 = "konstantynopolitaneczka"
        result = equal_strings(s1, s2)
        TaskTest.logger.log_single_test_result("should_compare_two_identical_strings", result == True)
        self.assertEqual(True, result)

    def test_should_compare_two_different_strings(self):
        s1 = "konstantynopolitaneczka"
        s2 = "some other string"
        result = equal_strings(s1, s2)
        TaskTest.logger.log_single_test_result("should_compare_two_different_strings", result == False)
        self.assertEqual(False, result)

    def test_should_compare_two_empty_strings(self):
        s1 = ""
        s2 = ""
        result = equal_strings(s1, s2)
        TaskTest.logger.log_single_test_result("should_compare_two_empty_strings", result == True)
        self.assertEqual(True, result)

    def test_should_compare_two_strings_where_one_is_null(self):
        s1 = "konstantynopolitaneczka"
        s2 = ""
        result = equal_strings(s1, s2)
        TaskTest.logger.log_single_test_result("should_compare_two_strings_where_one_is_null", result == False)
        self.assertEqual(False, result)

    def test_should_compare_empty_string_and_null_string(self):
        s1 = ""
        s2 = None
        result = equal_strings(s1, s2)
        TaskTest.logger.log_single_test_result("should_compare_empty_string_and_null_string", result == True)
        self.assertEqual(True, result)

    def test_should_compare_two_null_strings(self):
        s1 = None
        s2 = None
        result = equal_strings(s1, s2)
        TaskTest.logger.log_single_test_result("should_compare_two_null_strings", result == True)
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()

