import unittest


def slow_multiply(mult, multiplier):
    if multiplier == 1:
        return mult

    return mult + slow_multiply(mult, multiplier - 1)


def fast_multiply(mult, multiplier):
    """
    This solution takes into advantage the other ways you can multiply.
    for e.g.
    2 * 3
    If you draw matrix of 2 * 3, we can just count the number of cells and we have the result but it would be slower O(a*b)
    However, if we could just count the half of the cells and double (If it is even) then we could get done with it
    :param mult:
    :param multiplier:
    :return: mult * multiplier
    """
    smaller = mult if mult < multiplier else multiplier
    bigger = multiplier if mult < multiplier else mult

    return _fast_multiply_helper(smaller, bigger)


def _fast_multiply_helper(smaller, bigger):
    if smaller == 0:
        return 0  # 0 * bigger = 0
    if smaller == 1:
        return bigger  # 1 * bigger = bigger

    # Half the smaller number
    half = smaller >> 1  # Divide by 2
    side_1 = _fast_multiply_helper(half, bigger)

    if smaller % 2 == 1:
        return side_1 + side_1 + bigger
    else:
        return side_1 + side_1


class TestMultiply(unittest.TestCase):
    def test_slow_multiply(self):
        self.assertEqual(slow_multiply(5, 4), 20)

    def test_fast_multiply(self):
        self.assertEqual(fast_multiply(17, 20), 340)
