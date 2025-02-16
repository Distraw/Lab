import unittest
from lab_5 import calculate_annual_increase

class TestCalculateAnnualIncrease(unittest.TestCase):
    def test_increasing_values(self):
        self.assertEqual(calculate_annual_increase([1, 2, 4, 16]), [100.0, 100.0, 300.0])

    def test_decreasing_values(self):
        self.assertEqual(calculate_annual_increase([100, 50, 25, 5]), [-50.0, -50.0, -80.0])

    def test_constant_values(self):
        self.assertEqual(calculate_annual_increase([999, 999, 999, 999]), [0.0, 0.0, 0.0])

    def test_mixed_values(self):
        self.assertEqual(calculate_annual_increase([50, 100, 50, 50]), [100.0, -50.0, 0.0])

    def test_single_value(self):
        self.assertEqual(calculate_annual_increase([5]), [])

    def test_zero_value(self):
        with self.assertRaises(ZeroDivisionError):
            calculate_annual_increase([0, 5])



if __name__ == '__main__':
    unittest.main()