f = open("BROTHERS.INP", "r")
g = open("BROTHERS.OUT", "w")


data = f.readlines()
n, m = map(int, data[0].split())
arr = []
for i in range(n):
    arr.append(list(map(int, data[i+1].split())))
    
    
def find_value_max(arr: list, pos: list, htr: list):
    x, y = map(int, pos)
    try:
        if arr[x+1][y] > arr[x][y+1] and [x+1, y] not in htr:
            htr.append([x+1, y])
            pos = [x+1, y]
            return arr[x+1][y], pos, htr
        else:
            htr.append([x, y+1])
            pos = [x, y+1]
            return arr[x][y+1], pos, htr
    except:
        try:
            htr.append([x, y+1])
            pos = [x, y+1]
            return arr[x][y+1], pos, htr
        except:
            htr.append([x+1, y])
            pos = [x+1, y]
            return arr[x+1][y], pos, htr 

a, b = 0, 0
htr = []

x, y = 0, 0
while x != n-1 or y != m-1: # An
    s, pos, htr = find_value_max(arr, [x, y], htr)
    x, y = map(int, pos)
    a += s    

x, y = 0, 0
while x != n-1 or y != m-1: # Bình
    s, pos, htr = find_value_max(arr, [x, y], htr)
    x, y = map(int, pos)
    b += s

print(a+b)
f.close(); g.close()