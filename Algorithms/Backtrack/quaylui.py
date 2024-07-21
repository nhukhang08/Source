f = open("input.txt", "r")
g = open("output.txt", "w")

def backtrack(i):
    for v in range(2):
        x.append(v)
        if i == n-1:
            print(*x, sep="")
        else:
            backtrack(i+1)
        x.pop()


n = int(f.readline())
x = []

backtrack(0)

f.close(); g.close()
