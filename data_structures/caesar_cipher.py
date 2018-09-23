import unittest


class CaesarCipher():
    """
    The Caesar Cipher implementation for uppercase letters only
    """

    def __init__(self, shift):
        """
        Takes a shift which is used as an offset for rotating a character
        :param shift:
        """
        self._shift = shift
        self.encoder = [None] * 26
        self.decoder = [None] * 26

        # Initialize the encode and decorder's

        for i in range(26):
            self.encoder[i] = chr((i + self._shift) % 26 + ord('A'))
            self.decoder[i] = chr((i - self._shift) % 26 + ord('A'))

    def encode(self, inp):
        """
        Encode the string with the caesar cipher shift and return the encoded string
        :param inp: string to be encoded
        :return: encoded string
        """
        if not inp:
            return
        encoded = []
        for i in range(len(inp)):
            if inp[i].isupper():
                encoded.append(self.encoder[ord(inp[i]) - ord('A')])
            else:
                encoded.append(inp[i])

        return ''.join(encoded)

    def decode(self, inp):
        """
        Decode the string with the caesar cipher shift and return the decoded string
        :param inp: string to be decoded
        :return: decoded string
        """
        if not inp:
            return
        decoded = []
        for i in range(len(inp)):
            if inp[i].isupper():
                decoded.append(self.decoder[ord(inp[i]) - ord('A')])
            else:
                decoded.append(inp[i])

        return ''.join(decoded)


class TestCaesarCipher(unittest.TestCase):

    def setUp(self):
        self.cipher = CaesarCipher(3)

    def test_cipher(self):
        output = 'WKH HDJOH LV LQ SODB; PHHW DW MRH\’V'
        inp = 'THE EAGLE IS IN PLAY; MEET AT JOE\’S'
        self.assertEqual(inp, self.cipher.decode(self.cipher.encode(inp)))
