#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install dsc40graph # Only run if you don't have dsc40graph
import dsc40graph
from collections import deque


# In[2]:


def assign_good_and_evil(graph):
    if len(graph.edges) == 0:
        return None
    status = {node: 'undiscovered' for node in graph.nodes}
    dic = {node: 'good' for node in graph.nodes}
    for node in graph.nodes:
        if status[node] == 'undiscovered':
            helper(graph, node, dic, status)
    return helper2(dic, graph)


# In[3]:


def helper(graph, source, dic, status=None):
    
    status = {node: 'undiscovered' for node in graph.nodes}
    
    status[source] = 'pending'
    pending = deque([source])
    
    while pending:
        u = pending.popleft()
        for v in graph.neighbors(u):
            if status[v] == 'undiscovered':
                pending.append(v)
                if dic[u] == 'good':
                    dic[v] = 'evil'
                else:
                    dic[v] = 'good'
                status[v] = 'pending'
        status[u] = 'visted'
    return dic


# In[4]:


def helper2(dic, graph):
    for node in graph.nodes:
        for v in graph.neighbors(node):
            if dic[node] == dic[v]:
                return None
    return dic

def main():
    # Testing
    example_graph = dsc40graph.UndirectedGraph()
    example_graph.add_edge('Michigan', 'OSU')
    example_graph.add_edge('USC', 'OSU')
    example_graph.add_edge('USC', 'UCLA')
    example_graph.add_node('UCSD')
    print(assign_good_and_evil(example_graph))


if __name__ == '__main__':
    main()