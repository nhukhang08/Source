with open("TONGSOLAP.INP", "r") as file:
    lines = file.readlines()
    t = int(lines[0])

g = open("TONGSOLAP.OUT", "w")

MOD = 10**6 + 7
for i in range(1, len(lines)):
    n, k = map(int, lines[i].split())
    result = 0
    for i in range(1, n+1):
        num = int(str(k) * i) % MOD
        result += num

    g.write(str(result) + "\n")

g.close()
