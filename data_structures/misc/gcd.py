import unittest


def find_gcd(x, y):
    while y:
        x, y = y, x % y

    return x


class TestGCD(unittest.TestCase):
    def test_find_gcd(self):
        self.assertEqual(find_gcd(35, 10), 5)
