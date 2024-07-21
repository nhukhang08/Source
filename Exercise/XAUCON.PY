f = open("XAUCON.INP", "r")
g = open("XAUCON.OUT", "w")

s = str(f.readline())

arr = []
for i in range(len(s)):
    for j in range(i+1, len(s)):
        ch = s[i:j]
        if ch not in arr:
            arr.append(ch)

g.write(f"{len(arr)}")
f.close(); g.close()