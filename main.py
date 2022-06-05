def main():    
    firstLine = list(map(int,input().split()))
    n, k = firstLine[0], firstLine[1]
    secondLine = list(map(int, input().split()))

    adj = {}
    for i in range(1, n+1):
        adj[i] = []

    for i in range(n-1):
        line = list(map(int, input().split()))
        adj[line[0]].append(line[1]), adj[line[1]].append(line[0])

main()
