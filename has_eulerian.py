#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install dsc40graph # Only run if you don't have dsc40graph
import dsc40graph
from collections import deque


# In[2]:


def has_eulerian(graph):
    if len(graph.edges) == 0:
        return None
    status = {node: 'undiscovered' for node in graph.nodes}
    for node in graph.nodes:
        if (len(graph.neighbors(node)) == 0) | (len(graph.neighbors(node)) % 2 == 1):
            return False
        if status[node] == 'undiscovered':
            dfs(graph, node, status)
    return True


# In[3]:


def dfs(graph, u, status):
    if status is None:\
        tatus = {node: 'undiscovered' for node in graph.nodes}

    status[u] = 'pending'
    for v in graph.neighbors(u):
        if status[v] == 'undiscovered':
            dfs(graph, v, status)

    status[u] = 'visted'


def main():
# Testing\n",
    test = dsc40graph.UndirectedGraph()
    for u, v in [(1,2),(2,3),(3,4),(4,5),(5,1)]:
        test.add_edge(u, v)
    print(test)
    print(has_eulerian(test))


if __name__ == '__main__':
    main()