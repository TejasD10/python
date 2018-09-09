from LinkedList import LinkedList


def remove_dups(l_list):

    if not l_list.head():
        return

    seen = set([l_list.head().value()])
    current = l_list.head()
    while current.next():
        if current.next().value() in seen:
            current._next = current.next().next()
            continue
        seen.add(current.next().value())
        current = current.next()


def remove_dups_followup(l_list):
    """
    Without using a buffer (set) in the upper case
    :param l_list:
    :return: Linkedlist with no duplicate elements
    """
    if not l_list:
        return

    curr = l_list.head()
    while curr:
        runner = curr.next()
        prev = curr
        while runner:
            if runner.value() == curr.value():
                prev._next = runner.next()

            runner = runner.next()
            prev = prev.next()
        curr = curr.next()


def main():
    """
    Responsible for creating a linked list and calling remove_dups
    :return:
    """
    l_list = LinkedList()
    l_list.add_to_list([1, 2, 3, 2])
    # remove_dups(l_list)
    remove_dups_followup(l_list)
    print(l_list)




if __name__ == '__main__':
    main()
