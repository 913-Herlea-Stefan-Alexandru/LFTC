from Node import Node
from Constants import INITIAL_CAPACITY

class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0

        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)

        hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        self.size += 1

        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            return

        prev = node
        while node is not None:
            if node.key == key:
                raise Exception("Key already exists!")
            prev = node
            node = node.next

        prev.next = Node(key, value)

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return -1
        else:
            return node.value
