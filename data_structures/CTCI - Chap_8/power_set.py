import unittest
import copy


def power_set(input):
    """
    Returns a power set(subsets) for the given input set
    :param input:
    :return:
    """
    if not input:
        return [[]]

    first = input.pop(0)  # Take the first element out
    result = power_set(input)
    out = copy.deepcopy(result)
    for item in out:
        item.insert(0, first)

    # Add each item from out to the result
    for i in out:
        result.append(i)
    return result


class TestPowerSet(unittest.TestCase):
    def setUp(self):
        self.input = [1, 2, 3]

    def test_power_set(self):
        result = power_set(self.input)
        print(result)
        self.assertEqual(len(result), 8)
