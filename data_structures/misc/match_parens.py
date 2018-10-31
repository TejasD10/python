"""
Match paranthesis '(' and ')' and '*', '*' can be taken as either of the paranthesis
or null if not required
"""
import unittest


def match_parens(input):
    if not input:
        return True
    if input[0] == ')' or input[-1] == '(':
        # Invalid input, return False
        return False

    left_count = 0
    right_count = 0
    star_count = 0

    for ch in input:
        if ch == '(':
            left_count += 1
        elif ch == ')':
            right_count += 1
        elif ch == '*':
            star_count += 1
        else:
            # No other value allowed
            return False

    if left_count - right_count == 0:
        return True
    rem = abs(left_count - right_count)
    if rem >= star_count:
        return True
    return False


class TestMatchParens(unittest.TestCase):
    def test_match_parens(self):
        self.assertTrue('(*)(*)(**')
        self.assertTrue('**')
        self.assertTrue('(*, *)')
        self.assertTrue('(*)')
