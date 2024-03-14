from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # A dictionary to keep track of all original nodes to their respective clones.
        oldToNew = {}

        # Define the DFS function that will clone the graph.
        def clone(node):
            # If the node has already been cloned, return the clone.
            if node in oldToNew:
                return oldToNew[node]

            # Clone the node (without neighbors initially) and record it in the dictionary.
            copy = Node(node.val)
            oldToNew[node] = copy

            # Iterate through all neighbors of the node, clone them recursively,
            # and add them to the neighbors list of the clone.
            for neigh in node.neighbors:
                copy.neighbors.append(clone(neigh))

            # Return the cloned node.
            return copy

        # Start the cloning process from the given node, or return None if the node is null.
        return clone(node) if node else None

'''
The clone function uses DFS to visit each node, clone it, and visit all its neighbors recursively, 
ensuring that every part of the graph is cloned correctly. The oldToNew dictionary maps original nodes to their clones, 
which helps avoid infinite loops and ensures that every node is only cloned once, preserving the graph's structure.
'''
