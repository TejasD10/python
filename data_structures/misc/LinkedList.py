class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)


class LinkedList(object):

    def __init__(self):
        self.head = None

    def insert(self, data):
        # Inserting into a Linked list
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = Node(data)

    def display(self):
        if not self.head:
            print('Empty List')
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next

    def removeDuplicates(self, root):
        if not root:
            return
        newlist = list()
        curr = root

        while curr:
            if curr.data not in newlist:
                newlist.append(curr.data)
            curr = curr.next

        self.head = None
        for item in newlist:
            self.insert(item)
        return self.head



def main():
    orig_list = LinkedList()
    orig_list.insert(10)
    orig_list.insert(20)
    orig_list.insert(10)
    orig_list.insert(40)
    # orig_list.display()
    orig_list.removeDuplicates(orig_list.head)
    orig_list.display()


if __name__ == '__main__':
    main()

