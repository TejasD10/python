class Range:
    """A class that mimics the built-in range class"""

    def __init__(self, start, stop=None, step=1):
        """Create the Range class with the start, stop and step"""

        if step == 0:
            raise ValueError('Step cannot be 0')

        if stop is None:
            start, stop = 0, start # Support range calls like Range(5)

        # length of the range
        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, item):
        if item < 0:
            item += len(self)

        if not 0 <= item < len(self):
            raise IndexError('Index out of range')

        return self._start + item * self._step
