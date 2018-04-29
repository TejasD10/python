from pprint import pprint as pp


def main(st=None):
    if st is None or st == "":
        return

    even = []
    odd = []
    for i in range(len(st)):
        if i % 2 == 0:
            even.append(st[i])
        else:
            odd.append(st[i])
    evenstr = ''.join(str(item) for item in even)
    oddstr = ''.join(str(item) for item in odd)
    print(evenstr, oddstr, sep=" ", end="")


def arrays():
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    for i in reversed(arr):
        print(str(i) + " ",end="")


def phonebook():
    numentries = int(input().strip())
    phonebook = {}
    for i in range(numentries):
        key, value = input().strip().split(' ')
        phonebook[key] = value

    while True:
        try:
            findstr = input().strip()
        except EOFError:
            break
        if not findstr:
            break
        res = phonebook.get(findstr)
        if res is None:
            print('Not Found')
        else:
            print('{}={}'.format(findstr,phonebook[findstr]))

    pp(phonebook)


def binary(n = None):
    """
    :param n: Base 10 integer to be converted into Binary
    :return: Binary representation of the input N -> str
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    binrep = []
    while n >= 1:
        binrep.append(n % 2)
        n = n // 2
    currcount = 0
    maxcount = 0
    for item in binrep:
        if item == 1:
            currcount += 1
        else:
            maxcount = max(currcount, maxcount)
            currcount = 0

    maxcount = max(currcount, maxcount)
    return maxcount
    # ''.join(str(i) for i in reversed(binrep))


def test():
    s = input().strip()
    try:
        print(int(s))
    except:
        print('Bad String')
if __name__ == '__main__':
    # main('Hacker')
    # arrays()
    # phonebook()
    # print(binary(13))
    test()