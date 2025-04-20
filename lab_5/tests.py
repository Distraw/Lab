import unittest
import torch
from numpy.ma.testutils import assert_equal

from tensor_operations import create_random_filled_tensor
from tensor_operations import get_positive_numbers_amount

class TestMatrixOperations(unittest.TestCase):
    def test_create_random_filled_tensor(self):
        arr = create_random_filled_tensor(3, 4, -5, 6)
        assert_equal(arr.shape, (3, 4))

        arr = create_random_filled_tensor(1, 1, -5, 6)
        assert_equal(arr.shape, (1, 1))

    def test_get_positive_numbers_amount(self):
        arr = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        assert_equal(get_positive_numbers_amount(arr), 9)

        arr = torch.tensor([[-1, -2, 0], [-4, -5, -6], [-7, -8, 0]])
        assert_equal(get_positive_numbers_amount(arr), 0)

        arr = torch.tensor([[-1, -2, 0], [-4, 5, -6], [7, -8, 0]])
        assert_equal(get_positive_numbers_amount(arr), 2)


if __name__ == '__main__':
    unittest.main()