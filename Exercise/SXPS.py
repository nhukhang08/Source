f = open("SXPS.INP", "r") 
g = open("SXPS.OUT", "w")

n, k = map(int, f.readline().split())

phanso = []
dec = []
for i in range(n+1):
    for j in range(i+1, n+1):
        if i/j not in dec:
            phanso.append(f"{i}/{j}")
            dec.append(i/j)


def sapxep(arr: int, lst: str):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

result = sapxep(dec, phanso)
g.write(result[k-1])
f.close(); g.close()

