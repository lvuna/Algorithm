from typing import Union
from Heap import HeapNode
from utils.helper import *

"""utils class to generate graph"""


class Edge:
    """
    Graph's edge
    """
    src: "Node"
    dst: "Node"

    def __init__(self, src: "Node", dst: "Node") -> None:
        self.src = src
        self.dst = dst

    def __str__(self) -> str:
        result = f'[{self.src} {self.dst}]'
        return result


class WeightedEdge(Edge, HeapNode):
    """
    edge with weight
    """

    weight: int

    def __init__(self, src: "Node", dst: "Node", weight: int):
        super().__init__(src, dst)
        self.weight = weight

    def __str__(self) -> str:
        result = f'[{self.src} {self.dst}] {self.weight}'
        return result

    def __eq__(self, other: "WeightedEdge") -> bool:
        if self.weight == other.weight:
            return True
        else:
            return False

    def __gt__(self, other: "WeightedEdge") -> bool:
        if self.weight > other.weight:
            return True
        else:
            return False

    def __lt__(self, other: "WeightedEdge") -> bool:
        if self.weight < other.weight:
            return True
        else:
            return False


class Node:

    """
    Graph's node
    """
    name: str
    distance: float
    f_time: int
    color: str
    parent: Union["Node", None]

    def __init__(self, name: str) -> None:
        self.name = name
        self.parent = None
        self.color = "white"
        self.distance = float("inf")
        self.f_time = float("inf")
        self.edge = []
        self.neighbour = []

    def __str__(self) -> str:
        result = f'{self.name}'
        return result

    def __eq__(self, other) -> bool:
        return self is other

    def add_edge(self, edge: "Edge") -> None:
        self.edge.append(edge)

    def get_edge(self) -> List["Edge"]:
        return self.edge


class Graph:

    """
    Graph
    """

    def __init__(self):
        self.node = []
        self.edge = []
        self.num_node = 0

    def random_generate(self, node_list: List[str], num: int, typ: str="") -> None:
        self.generate_node(node_list)
        if typ == "w":
            self.random_generate_weight_edge(num)
        else:
            self.random_generate_edge(num)

    def generate_node(self, name_list: List[str]) -> None:
        for name in name_list:
            node = Node(name)
            self.node.append(node)
            self.num_node += 1

    def random_generate_weight_edge(self, num: int) -> None:

        if num > self.num_node ** (self.num_node - 1):
            raise Exception("edge count greater than maximum number of possible")

        while num != 0:
            nodes = choose_index(self.num_node)
            src = self.node[nodes[0]]
            dst = self.node[nodes[1]]
            weight = randint(1, 20)
            new_edge = WeightedEdge(src, dst, weight)

            while self.check_edge(new_edge):
                nodes = choose_index(self.num_node)
                src = self.node[nodes[0]]
                dst = self.node[nodes[1]]
                weight = randint(1, 20)
                new_edge = WeightedEdge(src, dst, weight)

            self.edge.append(new_edge)
            src.add_edge(new_edge)
            src.neighbour.append(dst)
            num -= 1

    def random_generate_edge(self, num: int) -> None:

        if num > self.num_node * (self.num_node - 1):
            raise Exception("edge count greater than maximum number of possible")
        # The current version is very slow as the edge count get close to the number of possible edges
        # Change this later
        while num != 0:
            nodes = choose_index(self.num_node)
            src = self.node[nodes[0]]
            dst = self.node[nodes[1]]
            new_edge = Edge(src, dst)

            while self.check_edge(new_edge):
                nodes = choose_index(self.num_node)
                src = self.node[nodes[0]]
                dst = self.node[nodes[1]]
                new_edge = Edge(src, dst)

            self.edge.append(new_edge)
            src.add_edge(new_edge)
            src.neighbour.append(dst)
            num -= 1

    def check_edge(self, new_edge: "Edge") -> bool:
        if not self.edge:
            return False

        for edge in self.edge:
            if check_for_same_edge(edge, new_edge):
                return True
        return False

    def find_node(self, name: str) -> Node:
        for node in self.node:
            if node.name == name:
                return node
        return None

    def print_graph(self) -> None:
        for node in self.node:
            edges = node.get_edge()
            edges_name = ""
            for edge in edges:
                edges_name += f'{edge} '
            message = f'{node} {node.distance} {node.f_time}: {edges_name}\n'
            print(message)


if __name__ == "__main__":
    test = Graph()
    test.random_generate(["a", "b", "c", "d"], 7, "w")
    test.print_graph()
