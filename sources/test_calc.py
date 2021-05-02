import unittest
import calc


class TestCalc(unittest.TestCase):
    # def test_input_no(self):
    #     x = int(input())
    #     y = int(input())
    #     with self.assertRaises(ValueError):
    #         calc.input_no(x, y)

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_substract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)


if __name__ == "__main__":
    unittest.main()
