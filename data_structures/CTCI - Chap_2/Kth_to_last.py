from .LinkedList import LinkedList


def kth_to_last(l_list, k=1):
    """
    Find the Kth to last element in the provided linked list
    :param l_list: Linked list
    :param k: a non-negative value less than the size of the list
    :return: The Kth to last element in the list
    """



def main():
    l_list = LinkedList()
    l_list.generate_list(5, 1, 15)
    kth_to_last(l_list, 2)


if __name__ == '__main__':
    main()
