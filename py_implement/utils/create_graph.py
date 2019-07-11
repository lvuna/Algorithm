from helper import *

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

    def __eq__(self, other: "Edge") -> bool:
        if self.src == other.src and self.dst == other.dst:
            return True
        else:
            return False


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
        self.edge = []
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
        # The current version is very slow as the edge count get close to the number of possible edges
        # Change this later
        while num != 0:
            nodes = choose_index(self.num_node)
            src = self.node[nodes[0]]
            dst = self.node[nodes[1]]
            new_edge = Edge(src, dst)

            while not self.check_edge(new_edge):
                nodes = choose_index(self.num_node)
                src = self.node[nodes[0]]
                dst = self.node[nodes[1]]
                new_edge = Edge(src, dst)

            self.edge.append(new_edge)
            src.add_edge(new_edge)
            num -= 1

    def check_edge(self, new_edge: "Edge") -> bool:
        if self.edge == []:
            return True

        for edge in self.edge:
            if new_edge == edge:
                return False
            else:
                return True

    def print_graph(self) -> None:
        for node in self.node:
            edges = node.get_edge()
            message = f'{node.name}: {edges}\n'
            print(message)


if __name__ == "__main__":
    test = Graph()
    test.random_generate(["a", "b", "c", "d"], 7)
    test.print_graph()