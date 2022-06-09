import main
import tree
import timeit

def test1(find_max):
    values = [1, 1, -1, -1, -1]
    n, k = (5, 2)
    edges = [(1, 2), (2, 3), (4, 1), (4, 5)]
    output = 2
    nodes = tree.construct(values, edges, n)
    main.construct_dp(n, k)
    root = nodes[0]
    return output == find_max(root, k)

def test2(find_max):
    values = [10, 2, 20, 1, 10, -25, 3, 4]
    n, k = (8, 2)
    edges = [(1, 2), (2, 3), (2, 4), (5, 1), (5, 6), (6, 7), (6, 8)]
    output = 43
    nodes = tree.construct(values, edges, n)
    main.construct_dp(n, k)
    root = nodes[0]
    return output == find_max(root, k)

def test3(find_max):
    values = [3, 5, -1, -2, -6, 4, 1]
    n, k = (7, 2)
    edges = [(1, 2), (2, 3), (2, 4), (1, 5), (5, 6), (5, 7)]
    output = 7
    nodes = tree.construct(values, edges, n)
    main.construct_dp(n, k)
    root = nodes[0]
    return output == find_max(root, k)

def test4(find_max):
    values = [3, -5, -1, -2, -6, 4, 1]
    n, k = (7, 2)
    edges = [(1, 2), (2, 3), (2, 4), (1, 5), (5, 6), (5, 7)]
    output = 3
    nodes = tree.construct(values, edges, n)
    main.construct_dp(n, k)
    root = nodes[0]
    return output == find_max(root, k)

def test5(find_max):
    values = [8, 4, -6, 5, 2, -12, -3, 20, 2, -9, 10]
    n, k = (11, 3)
    edges = [(1, 2), (2, 3), (3, 4), (3, 5), (1, 6), (6, 7), (7, 8), (7, 9),
             (6, 10), (10, 11)]
    output = 21
    nodes = tree.construct(values, edges, n)
    main.construct_dp(n, k)
    root = nodes[0]
    return output == find_max(root, k)

def test6(find_max):
    values = [2, -4, 6, -3, 3, 4]
    n, k = (6, 0)
    edges = [(1, 2), (1, 3), (3, 4), (4, 5), (3, 6)]
    output = 8
    nodes = tree.construct(values, edges, n)
    main.construct_dp(n, k)
    root = nodes[0]
    return output == find_max(root, k)

def test7(find_max):
    values = [6, 4, -2, -3, 4, -4, -5]
    n, k = (7, 3)
    edges = [(1, 2), (2, 3), (2, 4), (1, 5), (5, 6), (5, 7)]
    output = 12
    nodes = tree.construct(values, edges, n)
    main.construct_dp(n, k)
    root = nodes[0]
    return output == find_max(root, k)

def test8(find_max):
    values = [-4, -6, -7]
    n, k = (3, 1)
    edges = [(1, 2), (1, 3)]
    output = -10
    nodes = tree.construct(values, edges, n)
    main.construct_dp(n, k)
    root = nodes[0]
    return output == find_max(root, k)

def test9(find_max):
    values = [-3, 6, -8, 7, -9, 2, -3, 1, 8, 7, -6, 7, 6, 9, -8, -12, -4, 2, 3]
    n, k = (19, 7)
    edges = [(1, 2), (2, 3), (3, 4), (4, 5), (3, 6), (6, 7), (6, 8), (1, 9),
             (9, 10), (10, 11), (11, 12), (10, 13), (13, 14), (13, 15),
             (9, 16), (16, 17), (17, 18), (17, 19)]
    output = 36
    nodes = tree.construct(values, edges, n)
    main.construct_dp(n, k)
    root = nodes[0]
    return output == find_max(root, k)

def test10(find_max):
    values = [-3]
    n, k = (1, 5)
    edges = []
    output = -3
    nodes = tree.construct(values, edges, n)
    main.construct_dp(n, k)
    root = nodes[0]
    return output == find_max(root, k)

def test11(find_max):
    values = [4, -2, 4, -8, 4]
    n, k = (5, 1)
    edges = [(1, 2), (1, 3), (3, 4), (4, 5)]
    output = 6
    nodes = tree.construct(values, edges, n)
    main.construct_dp(n, k)
    root = nodes[0]
    return output == find_max(root, k)

tests = [test1, test2, test3, test4, test5, test6, test7, test8, test9, test10,
         test11]


for i, test in enumerate(tests):
    start = timeit.default_timer()
    result = test(main.find_max_recursive)
    stop = timeit.default_timer()
    runtime = stop - start
    print(f"Recursive Algorithm #{i+1}: {result}, Run Time: {1000 * runtime:.3f} ms")


for i, test in enumerate(tests):
    start = timeit.default_timer()
    result = test(main.find_max_dp)
    stop = timeit.default_timer()
    runtime = stop - start
    print(f"Dynamic Programming Algorithm #{i+1}: {result}, Run Time: {1000 * runtime:.3f} ms")
