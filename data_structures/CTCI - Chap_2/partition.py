from misc.LinkedList import LinkedList


def partition(l_list, part_key):
    """
    Write code to partition a linked list around a value x, such that all nodes less than x come
    before all nodes greater than or equal to x. If x is contained within the list the values of x only need
    to be after the elements less than x (see below). The partition element x can appear anywhere in the
    "right partition"; it does not need to appear between the left and right partitions.
    :param l_list: Linked List to be partitioned
    :param part_key:Key around which the linked list should be partitioned
    :return: Reference to the newly created list
    """
    if not l_list:
        return
    left_start = left_end = right_start = None

    curr = l_list.head()
    left_start = LinkedList()
    right_start = LinkedList()
    while curr:
        if curr.value() < part_key:
            left_start.add_last(curr)
        else:
            right_start.add_last(curr)
        curr = curr.next()

    if not left_start.empty():
        left_end = left_start.tail()
        left_end._next = right_start.head()
    return left_start if not left_start.empty() else right_start


def main():
    l_list = LinkedList()
    # l_list.add_last(30)
    # l_list.add_last(10)
    # l_list.add_last(15)
    # l_list.add_last(5)
    # l_list.add_last(1)
    l_list.generate_list(5, 1, 20)
    print(partition(l_list, 7))


if __name__ == '__main__':
    main()
