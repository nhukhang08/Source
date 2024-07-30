with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())
s = [1]
for i in range(n):
    result = []
    while len(s)!=0:
        num = s.pop()
        result.append(2*num+1)
        result.append(3*num+1)
    s = result
result.sort()
with open("output.txt", "w") as g:
    g.write(str(result[m-1]))