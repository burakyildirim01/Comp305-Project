import tree

dp = []

def find_max_children_sum(curr, k, find_max):
    result = [find_max(curr.left, i) + find_max(curr.right, k-i) for i in range(k+1)]
    return max(result)

def find_max_recursive(curr, k):
    if curr.left is None:
        return curr.value

    if curr.right is None:
        if k > 0:
            return max(curr.value, find_max_recursive(curr.left, k) + curr.value)
        else:
            return curr.value + find_max_recursive(curr.left, 0)

    if k > 0:
        maximum = find_max_children_sum(curr, k, find_max_recursive)
        if k > 1:

            return max(find_max_recursive(curr.left, k-1) + curr.value, find_max_recursive(curr.right, k-1) + curr.value, curr.value + maximum,
                   curr.value)
        else:
            return max(find_max_recursive(curr.left, k-1) + curr.value, find_max_recursive(curr.right, k-1) + curr.value, curr.value + maximum)
    else:
        return find_max_recursive(curr.left, 0) + curr.value + find_max_recursive(curr.right, 0)

def find_max_dp(curr, k):
    if dp[curr.key - 1][k] is None:
        if curr.left is None:
            dp[curr.key - 1][k] = curr.value
            return curr.value

        if curr.right is None:
            if k > 0:
                dp[curr.key - 1][k] = max(curr.value, find_max_recursive(curr.left, k) + curr.value)
                return max(curr.value, find_max_recursive(curr.left, k) + curr.value)
            else:
                dp[curr.key - 1][k] = curr.value + find_max_recursive(curr.left, 0)
                return curr.value + find_max_recursive(curr.left, 0)

        if k > 0:
            maximum = find_max_children_sum(curr, k, find_max_recursive)
            if k > 1:
                dp[curr.key - 1][k] = max(find_max_recursive(curr.left, k-1) + curr.value, find_max_recursive(curr.right, k-1) + curr.value, curr.value + maximum,
                   curr.value)
                return max(find_max_recursive(curr.left, k-1) + curr.value, find_max_recursive(curr.right, k-1) + curr.value, curr.value + maximum,
                   curr.value)
            else:
                dp[curr.key - 1][k] = max(find_max_recursive(curr.left, k-1) + curr.value, find_max_recursive(curr.right, k-1) + curr.value, curr.value + maximum)
                return max(find_max_recursive(curr.left, k-1) + curr.value, find_max_recursive(curr.right, k-1) + curr.value, curr.value + maximum)
        else:
            dp[curr.key - 1][k] = find_max_recursive(curr.left, 0) + curr.value + find_max_recursive(curr.right, 0)
            return find_max_recursive(curr.left, 0) + curr.value + find_max_recursive(curr.right, 0)
    else:
        return dp[curr.key - 1][k] 

def construct_dp(n, k):
    for _ in range(n):
        temp = []
        for _ in range(k+1):
            temp.append(None)
        dp.append(temp)

def main():    
    first_line = list(map(int,input().split()))
    n, k = first_line[0], first_line[1]
    values = list(map(int, input().split()))
    
    construct_dp(n, k)

    edges = []
    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        edges.append((u, v))

    nodes = tree.construct(values, edges, n)
    root = nodes[0]

    print(find_max_recursive(root, k))
    print(find_max_dp(root, k))

if __name__ == "__main__":
    main()
