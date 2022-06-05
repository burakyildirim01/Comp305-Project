class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None




def findMax(curr, k):
    if curr.left is None:
        if(curr.value<0 and k>0):
            return 0
        return curr.value
    if curr.right is None:
        if(max(findMax(curr.left, k-1) + curr.value, findMax(curr.left, k) + curr.value)<0 and k>0):
            return 0
        return max(findMax(curr.left, k-1) + curr.value, findMax(curr.left, k) + curr.value)
    maximum = -1
    for i in range(k+1):
        result = findMax(curr.left, i) + findMax(curr.right, k-i)
        if(result > maximum):
            maximum = result
    return max(findMax(curr.left, k-1) + curr.value, findMax(curr.right, k-1) + curr.value,
        curr.value + maximum)






def main():    
    firstLine = list(map(int,input().split()))
    n, k = firstLine[0], firstLine[1]
    values = list(map(int, input().split()))
    root = Node(1, values[0])
    nodes = [root]
    relations = [] 
    
    for i in range(2, n+1):
        node = Node(i, values[i-1])
        nodes.append(node)
    
    for i in range(n-1):
        u, v = list(map(int, input().split()))
        relations.append((u, v))
    
    for i in relations:
        if(i[0] < i[1]):
            node = nodes[i[0] - 1]
            if(node.left is None):
                node.left = nodes[i[1] - 1]
            else:
                node.right = nodes[i[1] - 1]
        else:
            node = nodes[i[1] - 1]
            if(node.left is None):
                node.left = nodes[i[0] - 1]
            else:
                node.right = nodes[i[0] - 1]
    print(findMax(root, k))
main()
