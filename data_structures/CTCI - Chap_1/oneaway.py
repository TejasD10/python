import unittest


def check_replace(str1, str2):
    """
    Check if the strings are one replace away
    :param str1: String one of the input
    :param str2: String two of the input
    :return: Bool
    """
    found_diff = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if found_diff:
                return False
            found_diff = True
    return True


def check_insert(str1, str2):
    """
    e.g. Ple -> Pale
    Pale -> Pales

    :param str1: Input one from the string
    :param str2: Input two from the string, the longer of the two
    :return:
    """
    index1, index2 = 0, 0
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


def isoneaway(str1, str2):
    if not str1 or not str2:
        return False
    if len(str1) == len(str2):
        return check_replace(str1, str2)
    if (len(str1) + 1) == len(str2):
        return check_insert(str1, str2)
    if (len(str1) - 1) == len(str2):
        return check_insert(str2, str1)
    return False


class Test(unittest.TestCase):
    """
    Unit Test Cases
    Check if str1 and str2 are one edits away
    Check if making one edit in either strings will make it equal
    """
    data = [('pale', 'bale', True), ('pales', 'pale', True), ('pale', 'ple', True),
            ('pale', 'bae', False), (None, 'abc', False)]

    def test_isoneaway(self):
        for str1, str2, outcome in self.data:
            self.assertEqual(outcome, isoneaway(str1, str2))


if __name__ == '__main__':
    unittest.main()
