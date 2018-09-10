from LinkedList import LinkedList


def kth_to_last(l_list, k=1):
    """
    Find the Kth to last element in the provided linked list
    :param l_list: Linked list
    :param k: a non-negative value less than the size of the list
    :return: The Kth to last element in the list
    """
    if not l_list:
        return

    if k > len(l_list):
        return

    runner = l_list.head()
    for i in range(k):
        if runner.next(): # Prevent the runner to become None in case the last element is asked for.
            runner = runner.next()

    curr = l_list.head()
    while runner.next():
        runner = runner.next()
        curr = curr.next()

    return curr.value()


def kth_to_last_recursive(head, k):
    """
    Return kth to last element in the list recursively
    :param head: Head of the Linked list
    :param k: element index from the last that needs to be returned
    :return: kth to last element.
    """
    if not head:
        return 0

    index = kth_to_last_recursive(head.next(), k)

    if index == k:
        print(head.value())

    index += 1
    return index


def main():
    l_list = LinkedList()
    l_list.generate_list(5, 1, 15)
    print(l_list)
    # print(kth_to_last(l_list, 3))
    kth_to_last_recursive(l_list.head(), 4)


if __name__ == '__main__':
    main()
