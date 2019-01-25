'''
Input: Filename of a file containing a three-tuple per line representing a one-directional
       edge between the first number, the second number and the third number represents
       the edge's weight
    eg:
        1 2 5
        2 1 5
        1 3 2
        3 1 2

        NOTE: The nodes are assumed to be sequentially numbers starting at 1 with no
        skipped numbers in between 1 and the highest numbered node
Output:
'''

from collections import namedtuple
import heapq
from pprint import pprint
from math import inf
from sys import argv
from typing import List

Edge = namedtuple('Edge', ['other_node', 'weight'])

def read_input(fname: str):
    data = open(fname).read()
    lines = sorted(data.split('\n')[:-1])

    nodes = {}

    for ln in lines:
        source, target, weight = tuple(map(int, ln.split()))
        if source not in nodes:
            nodes[source] = []
        nodes[source].append(Edge(target, weight))

    keys = sorted(nodes.keys())
    adj_list = [None] * (len(nodes) + 1)
    for node in nodes:
        adj_list[node] = nodes[node]
    return adj_list


def dijkstra(start_node: int, graph: List[List[Edge]]):
    # Distance to each node from start node
    distances = [inf] * len(graph)
    distances[start_node] = 0

    # Set all nodes (1 to last node) to false
    processed_nodes = [False] * (len(graph) + 1)

    # Priority queue to keep track of which node to process next
    # NOTE: Python's builtin heapq priority queue implementation uses 0 based and is a
    # min-heap
    # Push starting node so we start with it
    next_node_to_process = [(0, start_node)]

    while len(next_node_to_process) > 0:
        _, node = heapq.heappop(next_node_to_process)

        # If already processed, don't do anything
        if processed_nodes[node]: continue
        processed_nodes[node] = True

        for edge in graph[node]:
            # If current node + edge weight is less than the current distance of the node
            # on the other side, we can reduce its distance
            if distances[node] + edge.weight < distances[edge.other_node]:
                # Set the distance of the node on the other side of the edge to the
                # distance of the current node + the edge weight
                distances[edge.other_node] = distances[node] + edge.weight
                # Push node on other side of the edge onto priority queue with a priority
                # value equal to its new distance
                heapq.heappush(
                    next_node_to_process,
                    (distances[edge.other_node], edge.other_node),
                )

    return distances


if __name__ == '__main__':
    graph = read_input(argv[1])
    pprint(dijkstra(1, graph))
