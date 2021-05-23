import unittest
from pkg.utils import plus, minus, multi

class UtilsTest(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(plus(3, 4), 7)

    def test_minus(self):
        self.assertEqual(minus(8, 7), 1)

    def test_multi(self):
        self.assertEqual(multi(5, 7), 35)

if __name__ == '__main__':
    unittest.main()
