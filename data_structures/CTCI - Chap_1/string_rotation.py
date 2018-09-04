import unittest


def is_string_rotation(s1, s2):
    """
    Assume you have a method i 5Su b 5 tr ing which checks if one word is a substring
    of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
    call to i5Sub5tring (e.g., "waterbottle" is a rotation of" erbottlewat").
    :return: bool - suggesting if s1 is a substring of s2 or not
    """

    # For the s2 to be a rotation of s1, it has to be of the same length

    if len(s1) == len(s2) != 0:
        return (s1 + s1).find(s2) != -1
    return False


class StringRotationTest(unittest.TestCase):
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False),
        ('', '', False)
    ]

    def test_is_string_rotation(self):
        for s1, s2, output in self.data:
            self.assertEqual(output, is_string_rotation(s1, s2))


if __name__ == '__main__':
    unittest.main()
