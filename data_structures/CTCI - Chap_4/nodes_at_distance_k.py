class Node:
    def __init__(self, value):
        self.data = value
        self.left = self.right = None

    def __str__(self):
        return str(self.data)

