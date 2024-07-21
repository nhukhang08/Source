def prime(x):
    if x in [2,3]:
        return True
    elif x < 2 or x % 2 == 0 or x % 3 == 0:
        return False
    else:
        for i in range(5, int(x**0.5)+1, 6):
            if x % i == 0 or x % (i+2) == 0:
                return False
    return True

with open("PRIMECOUNT.INP", "r") as f:
    n = int(f.readline())
    
    arr = []
    
    for _ in range(n):
        l, r = map(int, f.readline().split())

        c = 0
        for i in range(l, r+1):
            if prime(i):
                c+=1
        arr.append(c)

arr = arr[::-1]
with open("PRIMECOUNT.OUT", "w") as g:
    for i in range(n-1):
        g.write(str(arr[i]) + "\n")
    g.write(str(arr[-1]))

    


