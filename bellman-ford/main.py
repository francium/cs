# There may be a bug in either this implementation or the input.txt file (distance from 1
# to node 3 is being computed as -1 when it should be 3)

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


def bellman_ford(start_node: int, graph: List[List[Edge]]):
    # Distance to each node from start node
    distances = [inf] * len(graph)
    distances[start_node] = 0
    # Loop over each edge in graph N-1 times
    # So first loop over each node
    for node, edges in enumerate(graph):
        # Skip over the assumed to be null 0-index node
        if not node: continue
        # Then loop over each node's edges -- two loops b/c of how the graph is structured
        for edge in edges:
            # New distance is the min of
            #     the current distance of the node on the other end
            #   OR
            #     the current nodes distance plus weight of the edge connecting to node on
            #     the other side of the edge
            distances[edge.other_node] = min(
                distances[edge.other_node],
                distances[node] + edge.weight,
            )

    # Run N'th time and if a distance changes, then it means there is a negative cycle in
    # the graph
    for node, edges in enumerate(graph):
        # Skip over the assumed to be null 0-index node
        if not node: continue
        for edge in edges:
            if distances[edge.other_node] > distances[node] + edge.weight:
                print(f'Graph has a negative cycle on edge ({node}, {edge.other_node})')
    return distances


if __name__ == '__main__':
    graph = read_input(argv[1])
    pprint(bellman_ford(1, graph))
