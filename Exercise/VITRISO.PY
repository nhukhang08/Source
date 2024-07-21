f = open("VITRISO.INP", "r")
g = open("VITRISO.OUT", "w")

n = int(f.readline())
arr = list(map(int, f.readline().split()))

vitri = -1
s = -1


for i in range(len(arr)-1):
    a = arr[i]
    b = arr[i+1]
        
    if vitri != -1:
        s += b
        if s <= 0:
            vitri = -1
            s = -1
            if a+b>0:
                vitri = i
                s = a+b
    
    elif a+b > 0:
        vitri = i
        s = a+b

g.write(str(vitri+1))

f.close(); g.close() 
    
