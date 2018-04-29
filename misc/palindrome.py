class Solution:
    def __init__(self):
        self.queue = []
        self.stack = []

    def pushCharacter(self, char):
        self.stack.append(char)

    def enqueueCharacter(self,char):
        self.queue.append(char)

    def popCharacter(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def dequeueCharacter(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

