import random

import unittest


def insertion_sort(arr):
    """
    Performs an insertion sort on the input array
    :param arr: Input array
    :return: In place sorted array, O(N2) worst case time, and O(N) best case time where the input array is sorted
    """
    if not arr:
        return

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break


class TestInsertionSort(unittest.TestCase):

    def setUp(self):
        self.input_array = [random.randint(1, 100) for _ in range(5)]

    def check_sorted(self, arr):
        """
        Utility to test if the array is sorted
        :param arr: Input array
        :return: True if the array is stored, False otherwise
        :O(N) - Runs in linear time
        """
        if not arr:
            return False

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False

        return True

    def test_insertion_sort(self):
        print(f'Input Array: {self.input_array}')
        insertion_sort(self.input_array)
        print(f'Sorted Array: {self.input_array}')
        self.assertTrue(self.check_sorted(self.input_array))
