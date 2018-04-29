class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        """
        Calculates the maximum absolute difference between two integers
        for e.g.
        3
        1 2 5
        """
        if len(self.__elements) < 2:
            raise ValueError('Invalid length of elements')
        self.maximumDifference = 0
        for i in range(len(self.__elements)):
            for j in range(i + 1, len(self.__elements)):
                self.maximumDifference = max(abs(self.__elements[i] - self.__elements[j]), self.maximumDifference)


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)