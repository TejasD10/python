def substringsKdist(inputStr, num):
    if not inputStr:
        return []
    result = []
    for i in range(len(inputStr)):
        check = []
        if i + num <= len(inputStr):
            for j in range(num):
                check.append(inputStr[i + j])

            if check_unique(check, num):
                result.append(check)
    return result


def check_unique(inp, num):
    test = set(inp)

    return len(test) == num


if __name__ == '__main__':
    print(substringsKdist('abcd', 3))
