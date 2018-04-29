from pprint import pprint


class BubbleSort:

    def __init__(self, elements):
        self._elem = elements

    def sort(self):
        """
        Implement bubble sort on the array
        for e.g.
        2, 1, 3, 4

        :return: A tuple of numswaps and a sorted list
        """
        # calculate the size of the array once
        n = len(self._elem)
        numswaps = 0
        for i in range(n):
            for j in range(n - 1 - i):
                if self._elem[j] > self._elem[j + 1]:
                    temp = self._elem[j]
                    self._elem[j] = self._elem[j + 1]
                    self._elem[j + 1] = temp
                    numswaps += 1
        return numswaps, self._elem[:]

def main():
    bsort = BubbleSort([2,1,3,4])
    numswaps, sortedlist = bsort.sort()
    pprint(numswaps)


if __name__ == '__main__':
    main()