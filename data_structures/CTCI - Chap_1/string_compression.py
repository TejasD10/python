import unittest


def compress(inp_string):
    """
    Compress a given string changing contiguos characters in into character and number format
    e.g.
    aaabbb = a3b3
    aaab
    :param inp_string: String to be compressed
    :return: Compressed string or the original one, whichever is the shortest
    """
    if not inp_string:
        return None
    if len(inp_string) < 2:  # If the length of the string is less than one, input itself is the shorter string
        return inp_string

    counter = 0
    output = []
    for i in range(len(inp_string)):
        counter += 1

        # If the next character is crossing the length of the string or is not equal we need to append the string
        if ((i + 1) >= len(inp_string)) or (inp_string[i] != inp_string[i + 1]):
            output.append(inp_string[i])
            output.append(str(counter))
            counter = 0

    return ''.join(output) if len(output) < len(inp_string) else inp_string # Return the created string


class StringCompressTest(unittest.TestCase):
    """
    Test Cases for compressing the strings
    """
    data = [('aabbb', 'a2b3'),
            ('aabbccaa', 'aabbccaa'),
            ('', None), ('a', 'a'), (None, None)]

    def test_compress_string(self):
        for inp_string, output in self.data:
            self.assertEqual(output, compress(inp_string))


if __name__ == '__main__':
    unittest.main()