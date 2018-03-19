from doxybook.node import Node

class Cache:
    def __init__(self):
        self.cache = {}

    def add(self, key: str, value: Node):
        self.cache[key] = value

    def get(self, key: str) -> Node:
        if key in self.cache:
            return self.cache[key]
        else:
            raise IndexError('Key: ' + key + ' not found in cache!')