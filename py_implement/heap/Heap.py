"""The implementation of heaps"""
from math import floor, log, ceil


class HeapNode:
    """Heap's node, to make sure those that use heap will always have the key and value attribute"""

    def __eq__(self, other) -> bool:
        raise NotImplementedError("It should be implemented by the subclass")

    def __gt__(self, other) -> bool:
        raise NotImplementedError("It should be implemented by the subclass")

    def __lt__(self, other) -> bool:
        raise NotImplementedError("It should be implemented by the subclass")


class Heap:
    """The implementation of heap"""

    def __init__(self) -> None:
        self.heap = []

    def insert(self, node: object) -> None:
        raise Exception("to be implemented by subclass")

    def visualize(self) -> None:
        result = ""
        for i in range(len(self.heap)):
            if i + 1 == 2 ** floor(log(i + 1, 2) + 1) - 1:
                result += f'{self.heap[i]} \n'
            else:
                result += f'{self.heap[i]}   '

        print(result)



class MaxHeap(Heap):

    def __init__(self) -> None:
        super().__init__()

    def insert(self, node: object) -> None:
        self.heap.append(node)
        index = len(self.heap) - 1
        parent = int(floor(index // 2))
        while index != 0:
            if self.heap[index] > self.heap[parent]:
                self.heap[index] = self.heap[parent]
                self.heap[parent] = node
                index = parent
                parent = int(floor(index // 2))
            else:
                return

    def extract_max(self) -> object:
        if not self.heap:
            return None
        extracted = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        max_heapify(self.heap, 0)
        return extracted

    def max(self) -> object:
        if not self.heap:
            return

        return self.heap[0]


def max_heapify(lst: list, index: int) -> None:
    left = index * 2
    right = index * 2 + 1
    if left >= len(lst):
        return
    elif right >= len(lst):
        right = left

    # Declare the nodes
    max_node = lst[index]
    left_node = lst[left]
    right_node = lst[right]

    if left_node > max_node:
        max_node = left_node
    if right_node > max_node:
        max_node = right_node

    # switch the nodes
    if max_node == lst[index]:
        return
    elif max_node == left_node:
        lst[left] = lst[index]
        lst[index] = left_node
        max_heapify(lst, left)
    else:
        lst[right] = lst[index]
        lst[index] = right_node
        max_heapify(lst, right)


if __name__ == "__main__":
    test_heap = MaxHeap()
    test_heap.insert(2)
    test_heap.insert(4)
    test_heap.insert(3)
    test_heap.insert(9)
    test_heap.visualize()
    print(test_heap.extract_max())
    test_heap.visualize()
