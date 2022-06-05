class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def construct(values, edges, n):
    nodes = []
    for i in range(1, n+1):
        node = Node(i, values[i-1])
        nodes.append(node)
    
    for edge in edges:
        u, v = edge
        if u < v:
            node = nodes[u - 1]
            if node.left is None:
                node.left = nodes[v - 1]
            else:
                node.right = nodes[v - 1]
        else:
            node = nodes[v - 1]
            if node.left is None:
                node.left = nodes[u - 1]
            else:
                node.right = nodes[u - 1] 
    
    return nodes
