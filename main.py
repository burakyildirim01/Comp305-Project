import tree
dp = []
def find_max_children_sum(curr, k):
    maximum = -1
    for i in range(k+1):
        result = find_max_recursive(curr.left, i) + find_max_recursive(curr.right, k-i)
        if result > maximum:
            maximum = result

    return result

def find_max_recursive(curr, k):
    if curr.left is None:
        if curr.value < 0 and 0 < k:
            return 0
        return curr.value

    if curr.right is None:
        if max(find_max_recursive(curr.left, k-1) + curr.value, find_max_recursive(curr.left, k) + curr.value) < 0 and 0 < k:
            return 0
        return max(find_max_recursive(curr.left, k-1) + curr.value, find_max_recursive(curr.left, k) + curr.value)

    maximum = find_max_children_sum(curr, k)

    if 0 < k:
        return max(find_max_recursive(curr.left, k-1) + curr.value, find_max_recursive(curr.right, k-1) + curr.value, curr.value + maximum)
    return maximum + curr.value

def find_max_dp(curr, k):     
    if dp[curr.key - 1][k] is None:
        if curr.left is None:
            if curr.value < 0 and 0 < k:
                dp[curr.key - 1][k] = 0
                return 0
            dp[curr.key - 1][k] = curr.value
            return curr.value

        if curr.right is None:
            if max(find_max_dp(curr.left, k-1) + curr.value, find_max_dp(curr.left, k) + curr.value) < 0 and 0 < k:
                dp[curr.key - 1][k] = 0
                return 0
            dp[curr.key - 1][k] = max(find_max_dp(curr.left, k-1) + curr.value, find_max_dp(curr.left, k) + curr.value)
            return dp[curr.key - 1][k]

        maximum = find_max_children_sum_dp(curr, k)

        if 0 < k:
            dp[curr.key - 1][k] = max(find_max_dp(curr.left, k-1) + curr.value, find_max_dp(curr.right, k-1) + curr.value, curr.value + maximum)
            return dp[curr.key - 1][k]
        dp[curr.key - 1][k] = maximum + curr.value
        return maximum + curr.value
    else:
        return dp[curr.key - 1][k]

def find_max_children_sum_dp(curr, k):
    maximum = -1
    for i in range(k+1):
        result = find_max_dp(curr.left, i) + find_max_dp(curr.right, k-i)
        if result > maximum:
            maximum = result
    
    return result

def main():    
    first_line = list(map(int,input().split()))
    n, k = first_line[0], first_line[1]
    for i in range(n):
        temp = []
        for _ in range(k+1):
            temp.append(None)
        dp.append(temp)
    values = list(map(int, input().split()))
    
    edges = []
    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        edges.append((u, v))

    nodes = tree.construct(values, edges, n)
    root = nodes[0]

    print(find_max_recursive(root, k))
    print(find_max_dp(root, k))

main()
