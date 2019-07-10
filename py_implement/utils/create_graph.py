from helper import *

"""utils class to generate graph"""


class Edge:
    """
    Graph's edge
    """
    src: "Node"
    dst: "Node"

    def __init__(self, src: "Node", dst: "Node"):
        self.src = src
        self.dst = dst


class WeightedEdge(Edge):
    """
    edge with weight
    """

    weight: int

    def __init__(self, src: "Node", dst: "Node", weight: int):
        super().__init__(src, dst)
        self.weight = weight


class Node:

    """
    Graph's node
    """
    name: str

    def __init__(self, name: str) -> None:
        self.name = name
        self.edge = []

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
        self.num_node = 0

    def random_generate(self, node_list: List[str], num: int) -> None:
        self.generate_node(node_list)
        self.random_generate_edge(num)

    def generate_node(self, name_list: List[str]) -> None:
        for name in name_list:
            node = Node(name)
            self.node.append(node)
            self.num_node += 1

    def random_generate_edge(self, num: int) -> None:

        if num > self.num_node ** 2:
            raise Exception("edge count greater than maximum number of possible")
        #Implement tomorrow
        while num != 0:
            nodes = choose_index(self.num_node)
            src = self.node[nodes[0]]
            dst = self.node[nodes[1]]
            new_edge = Edge(src, dst)
            self.check_edge(new_edge)
            num -= 1

    def check_edge(self, edge: "Edge") -> None:
        
