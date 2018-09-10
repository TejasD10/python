from LinkedList import LinkedList


def delete_nth_node(node):
    """
    Delete the nth node in the list, This must not be the last element in the list
    :param node: reference to the node which is to be deleted
    :return:
    """
    if not node:
        return

    # Copy the value of the node.next() into node
    node._element = node.next().value()
    node._next = node.next().next()


def find_node(l_list, k):
    """
    Return the reference to the kth node in the list
    :param l_list: Linked List
    :param k: index of the node to be found
    :return: reference to the kth node in the list
    """
    if not l_list:
        return

    curr = l_list.head()
    for i in range(k):
        if curr is None or curr.next() is None:
            raise IndexError('Index out of bounds')
        else:
            curr = curr.next()

    return curr


def main():
    l_list = LinkedList()
    l_list.generate_list(5, 1, 20)
    node = find_node(l_list,3)
    print(f'Source List: {l_list}')
    delete_nth_node(node)
    print(f'Deleted list: {l_list}')


if __name__ == '__main__':
    main()