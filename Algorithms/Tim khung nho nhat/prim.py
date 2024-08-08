def find_min_index(d,  vh,  near):
    min_index = -1
    
    for i in range(1, len(d)):
        if i not in vh and near[i] != -1:
            if min_index == -1 or d[i] < d[min_index]:
                min_index = i
    return min_index


with open("input.txt", "r") as f:
    v, e = map(int, f.readline().split()); data = [list(map(int, line.split())) for line in f.readlines()]; f.close()

vo_cung = max(line[2] for line in data) + 1; arr = [[vo_cung] * (v+1) for _ in range(v+1)]
for x, y, w in data:
    arr[x][y] = arr[y][x] = w
s = 1
vh = [s]
T = []
d = [float('inf')] * (v + 1)
near = [-1] * (v + 1)
d[s] = 0
near[s] = s
for v in range(1, v + 1):
    if v != s:
        d[v] = arr[s][v]
        near[v] = s

for _ in range(v - 1):
    u = find_min_index(d, vh, near)
    vh.append(u)
    T.append((u, near[u]))

    for v in range(1, v + 1):
        if v not in vh and arr[u][v] < d[v]:
            d[v] = arr[u][v]
            near[v] = u
print(sum(arr[x][y] for x, y in T))