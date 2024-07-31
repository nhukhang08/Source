# m, n, k = map(int, input().split())
m, n, k = 9, 5, 3

"""




"""

t = "1"
for i in range(n):
    t = str(int(t)*m)
    if len(t) > k:
        t = t[len(t)-k:]
print(t)