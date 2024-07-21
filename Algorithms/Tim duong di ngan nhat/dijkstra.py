f = open("input.txt", "r")
g = open("output.txt", "w")

n, m, start = map(int, f.readline().split())
arr = [[float("inf")] * n for _ in range(n)]

for _ in range(m):
    x, y, w = map(int, f.readline().split())
    arr[x][y] = w

def dijkstra(arr:list, start):
    n = len(arr)
    d = [start] + [float("inf")] * (n-1)
    p = [False] * n
    
    for _ in range(n):
        u = -1
        min_w = float("inf")
        for i in range(n):
            if d[i] < min_w and p[i] == False:
                min_w = d[i]; u = i
        if u == -1:
            break
        p[u] = True
        for v in range(n):
            if arr[u][v] != float("inf") and p[v] == False:
                new_w = d[u] + arr[u][v]
                if new_w < d[v]:
                    d[v] = new_w
    result = {}
    for i in range(n):
        if d[i] == float("inf"):
            result[i] = -1
        else:
            result[i] = d[i]
    return result



result = dijkstra(arr, start)
for v, w in result.items():
    g.write(f"{v}: {w}\n")
f.close(); g.close()