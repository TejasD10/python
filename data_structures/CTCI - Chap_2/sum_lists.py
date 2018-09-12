from LinkedList import LinkedList


def sum_lists(l1, l2, carry):
    """
    You have two numbers represented by a linked list, where each node contains a single
    digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
    function that adds the two numbers and returns the sum as a linked list.
    EXAMPLE
        Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
        Output: 2 -> 1 -> 9. That is, 912.
        Input: (8-> 3) + (1 -> 1 -> 2).That is,211 + 38.
        Output: 9 -> 4 -> 2. That is, 249.
    :param l1: List 1
    :param l2: List 2
    :param carry: Carry over the sum in the current execution thread
    :return:
    """
    if not l1 and not l2 and carry == 0:
        return

    new_list = LinkedList()
    node_sum = carry + (l1.value() if l1 else 0) + (l2.value() if l2 else 0)
    new_list.add_last(node_sum % 10)
    result = sum_lists(l1.next() if l1 else None, l2.next() if l2 else None, node_sum // 10)
    new_list.add_last(result) if result else None

    return new_list


def main():
    l1 = LinkedList()
    l1.add_last(8)
    l1.add_last(3)

    l2 = LinkedList()
    l2.add_last(1)
    l2.add_last(1)
    l2.add_last(2)

    new_list = sum_lists(l1.head(), l2.head(), 0)
    print(new_list)


if __name__ == '__main__':
    main()
