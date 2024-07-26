'''
0: 0
1: 4
2: 1
3: 3
'''
f = open("input.txt", "r")

n, m, start = map(int, f.readline().split())

arr = [[float("inf")]*n for x in range(n)] 

for _ in range(m):
    x, y, w = map(int, f.readline().split())
    arr[x][y] = w

def tim_duong_di_ngan_nhat(arr:list, start:int):
    n = len(arr)
    d = [float("inf")] * n
    for i in range(n):
        if i == start:
            d[i] = start
    p = [False] * n
    
    for _ in range(n):
        u = -1
        min_u = float("inf")
        for i in range(n):
            if d[i] < min_u and p[i] == False:
                min_u = d[i]
                u = i
        
        if u == -1:
            break
        
        p[u] = True
        for v in range(n):
            if arr[u][v] < float("inf") and p[v] == False:
                new_w = d[u] + arr[u][v]
                if new_w < d[v]:
                    d[v] = new_w
    result = {}
    for i in range(n):
        if d[i] == float("inf"):
            result[i] == -1
        else:
            result[i] = d[i]
    return result
                    
            



for i, j in tim_duong_di_ngan_nhat(arr, start).items():
    print(f"{i}: {j}")
f.close()