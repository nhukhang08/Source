n = 4
arr = [2,3,1,4,5]

def bubblesort(arr):
    d = {}
    for i in range(n):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                if arr[i] in d:
                    d[arr[i]] += 1
                else:
                    d[arr[i]] = 1
    return arr, d

s = 0
kt = True
for _, num in bubblesort(arr)[1].items():
    if num > 2:
        kt = False
    s += num
if kt:
    print(s)
else:
    print(-1)