import unittest
from crime import get_max_increase

class TestGetMaxIncrease(unittest.TestCase):
    def test_table_from_task(self):
        self.assertEqual(get_max_increase([
            [40690, 29921, 24771, 27235, 33084],
            [3174, 2711, 3132, 4147, 5079],
            [7973, 7813, 8745, 11119, 13965],
            [51319, 45071, 41157, 44750, 56234]]),
            (75.15364354697103 / 100, 2))

if __name__ == '__main__':
    unittest.main()