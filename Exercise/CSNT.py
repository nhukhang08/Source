f = open("CSNT.INP", "r")
g = open("CSNT.OUT", "w")

L, R = map(int, f.readline().split())

def prime(x):
    if x in [2, 3]:
        return True
    elif x < 2 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, int(x**0.5)+1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True

arr = []
for i in range(L, R+1):
    if prime(i):
        arr.append(i)

g.write(str(len(arr))+ "\n")

for i in range(len(arr)-1):
    g.write(str(arr[i])+ " ")

g.write(str(arr[-1]))

g.close(); f.close()

