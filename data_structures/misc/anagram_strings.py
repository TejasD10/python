import unittest


def compare(p_hist, s_hist):
    if p_hist == s_hist:
        zeros = [0] * 256
        if p_hist == zeros and s_hist == zeros:
            return False
        else:
            return True


def find_anagrams_RP(s: str, p: str):
    # abab
    # ab
    if not s:
        return []

    p_len = len(p)
    s_len = len(s)

    if p_len > s_len:
        return []
    result = []
    p_hist = [0] * 256
    s_hist = [0] * 256

    for i in range(p_len):
        p_hist[ord(p[i])] += 1
        s_hist[ord(s[i])] += 1

    for i in range(p_len, s_len):
        if compare(p_hist, s_hist):
            result.append(i - p_len)

        # Add the new character
        s_hist[ord(s[i])] += 1
        # Remove the old character to continue the window
        s_hist[ord(s[i - p_len])] -= 1

    if compare(p_hist, s_hist):
        result.append(s_len - p_len)

    return result


def find_anagrams_in_string(string: str, p: str):
    if not string:
        return []
    ans = anagrams(p)
    result = []
    for i in range(len(string)):
        if string[i:(i + len(p))] in ans:
            result.append(i)
    return result


def anagrams(string):
    if not string:
        return []
    return _anagram_helper(string)


def _anagram_helper(string):
    if not string:
        return ['']
    perms = []

    first = string[0]
    rem = string[1:]

    words = _anagram_helper(rem)

    for word in words:
        for i in range(len(word) + 1):
            perms.append(word[:i] + first + word[i:])

    return perms


class TestAnagrams(unittest.TestCase):
    def test_anagrams(self):
        print(find_anagrams_RP('abab', 'ab'))
        print(find_anagrams_RP('aa', 'bb'))
