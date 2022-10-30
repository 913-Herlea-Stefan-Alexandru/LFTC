from Constants import INITIAL_CAPACITY
from domain.Node import Node
from tabulate import tabulate


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

        self.size += 1
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

    def get_table(self, key_header, value_header):
        data = []
        headers = [key_header, value_header]

        for bucket in self.buckets:
            if not bucket:
                continue
            node = bucket
            while node is not None:
                data.append([node.key, node.value])
                node = node.next

        return tabulate(data, headers=headers, tablefmt="grid")
