import unittest


def check_palindrome_permutation(input_string):
    if input_string is None or len(input_string) <= 1:
        return False

    # Enter the entries in a dict
    hist = {}
    oddCount = 0
    for i in range(len(input_string)):
        if input_string[i] != ' ':
            hist[input_string[i]] = hist[input_string[i]] + 1 if hist.get(input_string[i]) else 1
            if hist[input_string[i]] % 2 == 0:
                oddCount += 1
            else:
                oddCount -= 1

    return oddCount <= 1


class Test(unittest.TestCase):
    # Using lists for storing the input and the desired output.
    data = [('taco cat', True), ('zero rez', True), ('', False), ('A', False)]

    def test_check_palindrome_permutation(self):
        for input_string, output in self.data:
            self.assertEqual(output, check_palindrome_permutation(input_string))


if __name__ == '__main__':
    unittest.main()
