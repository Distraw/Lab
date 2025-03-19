import unittest
import numpy as np
from unittest.mock import patch

from lab_2.numpy_operations import input_numpy_array
from numpy_operations import get_elements_occuring_in_range_from_n_to_x_times

class TestGetElementsOccuringInRangeFromNToXTimes(unittest.TestCase):
    def test_n_values(self):
        np.testing.assert_array_equal(get_elements_occuring_in_range_from_n_to_x_times(
            np.array([0, 1, 2, 3, 4, 5]), 1, 5), np.array([]))

    def test_next_after_n_values(self):
        np.testing.assert_array_equal(get_elements_occuring_in_range_from_n_to_x_times(
            np.array([0, 1, 1, 2, 3, 4, 4, 5]), 1, 5), np.array([1, 4]))

    def test_x_values(self):
        np.testing.assert_array_equal(get_elements_occuring_in_range_from_n_to_x_times(
            np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]), 1, 5), np.array([]))

    def test_previous_before_x_values(self):
        def test_x_values(self):
            np.testing.assert_array_equal(get_elements_occuring_in_range_from_n_to_x_times(
                np.array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]), 1, 5), np.array([0, 1, 2, 3]))

    def test_empty_array(self):
        def test_x_values(self):
            np.testing.assert_array_equal(get_elements_occuring_in_range_from_n_to_x_times(
                np.array([]), 1, 5), np.array([]))

class TestInputNumpyArray(unittest.TestCase):
    @patch("builtins.input", side_effect=["4", "1", "2", "3", "4"])
    def test_input_array(self, mock_input):
        np.testing.assert_array_equal(input_numpy_array(), np.array([1, 2, 3, 4]))

    @patch("builtins.input", side_effect=["hello friend", "1", "2", "3", "4"])
    def test_invalid_input(self, mock_input):
        with self.assertRaises(ValueError):
            input_numpy_array()

if __name__ == '__main__':
    unittest.main()