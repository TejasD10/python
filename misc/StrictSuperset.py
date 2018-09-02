def main():
    set_a = [int(i) for i in input().split(' ')]
    num_sets = int(input())
    inputlists = []
    for num in range(num_sets):
        inputlist = [int(i) for i in input().split(' ')]
        inputlists.append(inputlist)

    # Is Strict Superset?
    return is_strict_superset(set_a, inputlists)


def is_strict_superset(set_a, inputlists):
    """

    :param set_a: Check of the Strict Superset
    :param inputlists: The lists to be checked against, if the set_a is the strict superset
    :return: True OR False - If the set_a is a strict superset or not.
    """
    len_set_a = len(set_a)
    issubset = True
    for item in inputlists:
        if len(item) < len_set_a:
            for i in item:
                if i not in set_a:
                    issubset = False
                    break
        else:
            issubset = False
            break

    return issubset


if __name__ =='__main__':
    print(main())