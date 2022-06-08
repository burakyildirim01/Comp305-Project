import main
import tree

def test1(find_max):
    values = [1, 1, -1, -1, -1]
    n, k = (5, 1)
    edges = [(1, 2), (2, 3), (4, 1), (4, 5)]
    output = 2
    nodes = tree.construct(values, edges, n)
    main.construct_dp(n, k)
    root = nodes[0]
    return find_max(root, k)

def test2(find_max):
    values = [10, 2, 20, 1, 10, -25, 3, 4]
    n, k = (8, 2)
    edges = [(1, 2), (2, 3), (2, 4), (5, 1), (5, 6), (6, 7), (6, 8)]
    output = 43
    nodes = tree.construct(values, edges, n)
    main.construct_dp(n, k)
    root = nodes[0]
    return find_max(root, k)

def test3(find_max):
    values = [1, 1, -1, -1, -1]
    n, k = (5, 2)
    edges = [(1, 2), (2, 3), (4, 1), (4, 5)]
    output = 2
    nodes = tree.construct(values, edges, n)
    main.construct_dp(n, k)
    root = nodes[0]
    return output == find_max(root, k)


print(test2(main.find_max_dp))
