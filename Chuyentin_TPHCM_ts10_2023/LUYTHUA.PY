f = open("LUYTHUA.INP", "r")
g = open("LUYTHUA.OUT", "w")

n = int(f.readline())
s = 0
for _ in range(n):
    inp = str(f.readline().strip())
    lenght = len(inp)

    num = int(inp[:lenght-1])
    pow = int(inp[-1])
    
    s += num ** pow

g.write(str(s))

f.close()
g.close()