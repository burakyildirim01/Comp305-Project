import tree 

def find_max_children_sum(curr, k):
    maximum = -1
    for i in range(k+1):
        result = find_max(curr.left, i) + find_max(curr.right, k-i)
        if result > maximum:
            maximum = result

    return result

def find_max(curr, k):
    if curr.left is None:
        if curr.value < 0 and 0 < k:
            return 0
        return curr.value

    if curr.right is None:
        if max(find_max(curr.left, k-1) + curr.value, find_max(curr.left, k) + curr.value) < 0 and 0 < k:
            return 0
        return max(find_max(curr.left, k-1) + curr.value, find_max(curr.left, k) + curr.value)

    maximum = find_max_children_sum(curr, k)

    return max(find_max(curr.left, k-1) + curr.value, find_max(curr.right, k-1) + curr.value, curr.value + maximum)

def main():    
    first_line = list(map(int,input().split()))
    n, k = first_line[0], first_line[1]
    values = list(map(int, input().split()))
    
    edges = []
    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        edges.append((u, v))

    nodes = tree.construct(values, edges, n)
    root = nodes[0]

    print(find_max(root, k))

main()
