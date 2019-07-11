"""The implementation of heaps"""


class Heap:
    """The implementation of heap"""

    def __init__(self) -> None:
        self.heap = []


class MaxHeap(Heap):

    def __init__(self) -> None:
        super().__init__()
    
    def extract_max(self) -> object:
        if not self.heap:
            return None
        extracted = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        return extracted
