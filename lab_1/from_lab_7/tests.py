import unittest
from database import process_command

class TestProcessCommand(unittest.TestCase):
    def test_exit(self):
        self.assertEqual(process_command("exit"), 0)

    def test_incorrect_values(self):
        self.assertEqual(process_command("exit here"), "Unknown command")
        self.assertEqual(process_command("asdawqeas"), "Unknown command")
        self.assertEqual(process_command("get unexisting_value"), "No such element in dictionary")

    def test_correct_values(self):
        self.assertEqual(process_command("add value1 that`s value 1"), "Element \"value1\" was added")
        self.assertEqual(process_command("get value1"), "that`s value 1")
        self.assertEqual(process_command("del value1"), "Element \"value1\" was deleted")
        self.assertEqual(process_command("get value1"), "No such element in dictionary")

if __name__ == '__main__':
    unittest.main()