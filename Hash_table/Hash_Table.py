"""Hash Table implementation"""

from typing import Union


class HashNode:
    """The node inside a hash-table, a linkedlist node to save computation for insert"""
    def __init__(self, key: int, value: object=None) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self) -> str:
        next_node = None
        previous_node = None
        if self.next is not None:
            next_node = self.next.key
        if self.previous is not None:
            previous_node = self.previous.key
        result = f'Node {self.key}: value: {self.value}, Next node:{next_node}, Previous node:{previous_node}'
        return result

    def __repr__(self) -> str:
        result = ""
        node = self
        while node is not None:
            result += f'{str(node.key)} '
            node = node.next
        return result


class HashTable:
    """The Hash table that resolves collision by chaining"""

    proportion: int

    def __init__(self, proportion: int) -> None:
        self.proportion = proportion
        self.num_items = 0
        self.container = [None]

    def insert(self, node: "HashNode") -> None:
        index = node.key % len(self.container)

        if self.container[index] is None:
            self.container[index] = node
        else:
            node.next = self.container[index]
            self.container[index].previous = node
            self.container[index] = node

        self.num_items += 1
        if self.num_items // len(self.container) > self.proportion:
            self.double()

    def delete(self, key: int) -> None:
        target = self.search(key)
        if target is None:
            return
        # If target is the first node in the linked-list
        if target.previous is None:
            index = self.hash(key)
            self.container[index] = target.next
        # If target is the last node in the linked-list
        elif target.next is None:
            target.previous.next = target.next
        # If target is a node in the middle
        else:
            target.previous.next = target.next
            target.next.previous = target.previous

        self.num_items -= 1
        if self.num_items // len(self.container) < self.proportion // 4:
            self.shrink()

    def search(self, key: int) -> Union["HashNode", None]:
        index = self.hash(key)
        node = self.container[index]
        while node is not None:
            if node.key == key:
                return node
            node = node.next
        print("No such key exists")
        return

    def shrink(self) -> None:
        new_container = []
        for _ in range(len(self.container) // 2):
            new_container.append(None)
        for node in self.container:
            rehash(node, new_container)
        self.container = new_container

    def double(self) -> None:
        new_container = []
        for _ in range(len(self.container) * 2):
            new_container.append(None)
        for node_list in self.container:
            rehash(node_list, new_container)
        self.container = new_container

    def visualize(self) -> None:
        for i in range(len(self.container)):
            if self.container[i] is not None:
                result = f'{i}: {visualize_node_list(self.container[i])}'
                print(result)

    def hash(self, key: int) -> int:
        return key % len(self.container)


def visualize_node_list(node: "HashNode") -> str:
    result = ""
    while node is not None:
        result += f'{str(node.key)} '
        node = node.next
    return result


def rehash(node_list: "HashNode", container: list) -> None:
    length = len(container)
    if node_list is None:
        return
    while node_list is not None:
        index = node_list.key % length
        new_node = HashNode(node_list.key, node_list.value)
        if container[index] is None:
            container[index] = new_node
        else:
            new_node.next = container[index]
            container[index].previous = new_node
            container[index] = new_node
        node_list = node_list.next


if __name__ == "__main__":
    table = HashTable(3)
    node1 = HashNode(4)
    node2 = HashNode(33)
    node3 = HashNode(22)
    node4 = HashNode(18)
    node5 = HashNode(14)
    table.insert(node1)
    table.insert(node2)
    table.insert(node3)
    table.insert(node4)
    table.insert(node5)
    table.insert(HashNode(325))
    table.insert(HashNode(123))
    table.insert(HashNode(2145))
    table.visualize()
    print()
    search_node1 = table.search(22)
    search_node2 = table.search(33)
    search_node3 = table.search(2145)
    print(search_node1)
    print(search_node2)
    print(search_node3)
