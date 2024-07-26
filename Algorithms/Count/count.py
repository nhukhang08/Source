f = open("input.txt", "r")
g = open("output.txt", "w")
arr = list(map(int, f.readline().split()))

def dem(arr):
    lst = {}
    for ch in arr:
        if ch in lst:
            lst[ch] += 1
        else:
            lst[ch] = 1
    return lst

for a, b in dem(arr).items():
    g.write(str(a)+": "+str(b)+"\n")


f.close(); g.close()