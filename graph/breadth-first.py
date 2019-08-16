from utils.create_graph import *


"""Implement the breadth first search algorithm."""


def breadth_first_search(graph: Graph, root: Node) -> None:
    # initialize the frontier
    # initialize the distance and color to infinity and white
    for node in graph.node:
        node.distance = float("inf")
        node.color = "white"
    root.distance = 0
    frontier = [root]
    while frontier:
        current_node = frontier.pop(0)
        for neighbour in current_node.neighbour:
            if neighbour.color == "white":
                neighbour.distance = current_node.distance + 1
                neighbour.parent = current_node
                neighbour.color = "grey"
                frontier.append(neighbour)
        current_node.color = "black"


def find_shortest_path(graph: Graph, root: Node, dst: Node) -> None:
    breadth_first_search(graph, root)
    if dst.parent is None:
        print("No path exists between 2 nodes")
        return
    result = ""
    while dst != root:
        temp = f" -> {dst.name}"
        temp += result
        result = temp
        dst = dst.parent
    print(root.name + result)


if __name__ == "__main__":
    graph1 = Graph()
    graph1.random_generate(["a", "b", "c", "d", "e", "f", "g", "h"], 17)
    graph1.print_graph()
    root_node = graph1.find_node("c")
    target = graph1.find_node("f")
    find_shortest_path(graph1, root_node, target)
