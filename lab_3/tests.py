import unittest
import numpy as np
from numpy.ma.testutils import assert_equal

from matrix_operations import create_random_filled_matrix
from matrix_operations import get_positive_numbers_amount

class TestMatrixOperations(unittest.TestCase):
    def test_create_random_filled_matrix(self):
        arr = create_random_filled_matrix(3, 4, -5, 6)
        assert_equal(arr.shape, (3, 4))

        arr = create_random_filled_matrix(1, 1, -5, 6)
        assert_equal(arr.shape, (1, 1))

    def test_get_positive_numbers_amount(self):
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        assert_equal(get_positive_numbers_amount(arr), 9)

        arr = np.array([[-1, -2, 0], [-4, -5, -6], [-7, -8, 0]])
        assert_equal(get_positive_numbers_amount(arr), 0)

        arr = np.array([[-1, -2, 0], [-4, 5, -6], [7, -8, 0]])
        assert_equal(get_positive_numbers_amount(arr), 2)


if __name__ == '__main__':
    unittest.main()