#!/usr/bin/env python
# coding: utf-8

# In[3]:


# pip install dsc40graph # Only run if you don't have dsc40graph
import dsc40graph


# In[43]:


def biggest_descendent(graph, root, value):
    if len(graph.edges) == 0:
        return None
    
    status = {node: 'undiscovered' for node in graph.nodes}
    for node in graph.nodes:
        if status[node] == 'undiscovered':
            dfs(graph, node, status, value)
    return value


# In[50]:


def dfs(graph, u, status, value):
    if status is None:
        status = {node: 'undiscovered' for node in graph.nodes}
    
    status[u] = 'pending'
    for v in graph.neighbors(u):
        if status[v] == 'undiscovered':
            dfs(graph, v, status, value)
            if value[v] > value[u]:
                value[u] = value[v]
    status[u] = 'visted'

def main():
    # Testing
    digraph = dsc40graph.DirectedGraph()
    for u, v in [(1,2),(1,3),(2,4),(2,5),(3,6),(3,7),(4,8),(4,9)]:
        digraph.add_edge(u, v)
    dic = {1:2,2:1,3:4,4:8,5:5,6:2,7:10,8:3,9:9}
    biggest_descendent(digraph, 1, dic)


if __name__ == '__main__':
    main()