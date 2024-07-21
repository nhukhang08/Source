f = open("CHUSO.INP", "r")
g = open("CHUSO.OUT", "w")

m, n, k = map(int, f.readline().split())

t = "1"
for i in range(n):   
    if len(t) < k:
        t = str(int(t) * m)
    else:
        t = str(int(t[len(t)-k:]) * m)

result = str(t[len(t)-k:])

if len(result) < k:
    result = "0" * ( k - len(result) ) + result

g.write(result)

f.close(); g.close()