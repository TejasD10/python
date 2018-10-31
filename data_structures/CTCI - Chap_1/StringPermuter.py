def main(inp = None):
    if input is None:
        raise ValueError('Invalid Input')

    print(permute(inp))


def permute(inp):
    perms = []
    if len(inp) == 0:
        perms.append('')
        return perms

    first = inp[0]
    rem = inp[1:]
    words = permute(rem)

    for word in words:
        for j in range(len(word) + 1):
            perms.append(insert_char_at(first,word,j))

    return perms


def insert_char_at(first, word ,j):
    return word[:j] + first + word[j:]


if __name__ == '__main__':
    inp = input()
    main(inp)