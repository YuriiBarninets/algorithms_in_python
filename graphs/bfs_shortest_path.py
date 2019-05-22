from graph import *


def bfs_shortest_path(graph, start_vertex, goal_vertex):
    """
    When we use BFS to find a shortest path we have to track path from source to goal.
    1. We may store parent vertex for each child, so this let us to get a path from goal to start
    when we hit a goal.
    2. We may store in queue list with path to vertex instead of single vertex, so the last item in list will
    represent a current vertex (we use this approach in the algorithm below)
    """
    if start_vertex == goal_vertex:
        return start_vertex

    # initially, queue contains only the list with start vertex
    # and all vertices are not visited
    queue = [[start_vertex]]
    visited_vertices = {}
    for vertex in graph.get_vertices():
        visited_vertices[vertex] = False

    while len(queue) > 0:
        # pop a vertex from the queue
        path_to_vertex = queue.pop(0)
        current_vertex = path_to_vertex[-1]

        # ignoring this vertex if it has been visited
        if visited_vertices[current_vertex.get_label()] is True:
            continue

        # return path to vertex if we find goal vertex
        if current_vertex == goal_vertex:
            return path_to_vertex

        # mark as visited, so we will not visit it anymore
        visited_vertices[current_vertex.get_label()] = True

        # get all adjacent vertices which HAVE NOT been visited
        adjacent_vertices = []
        for edge in current_vertex.get_outbound_edges():
            if visited_vertices[edge.get_end_vertex().get_label()] is False:
                adjacent_vertices.append(edge.get_end_vertex())

        # push a list with path to each adjacent vertex in our queue
        for adjacent_vertex in adjacent_vertices:
            new_path = path_to_vertex.copy()
            new_path.append(adjacent_vertex)
            queue.append(new_path)

    # return None if there no a path between start and goal vertices
    return None


if __name__ == "__main__":

    # vertices
    graph = Graph()
    graph.add_vertex("a")
    graph.add_vertex("b")
    graph.add_vertex("c")
    graph.add_vertex("d")
    graph.add_vertex("e")
    graph.add_vertex("f")

    # a --> b, a --> c, a --> d
    graph.add_edge("a", "b")
    graph.add_edge("a", "c")
    graph.add_edge("a", "d")

    # b --> c, b --> f
    graph.add_edge("b", "c")
    graph.add_edge("b", "f")

    # c --> d
    graph.add_edge("c", "d")

    # d --> e
    graph.add_edge("d", "e")

    # e --> f
    graph.add_edge("e", "f")

    a = graph.get_vertex("a")
    f = graph.get_vertex("f")
    shortest_path = bfs_shortest_path(graph, a, f)

    if shortest_path:
        for vertex in shortest_path:
            print(vertex)
    else:
        print("There no path between {0} & {1}".format(
            a.get_label(), f.get_label()))
