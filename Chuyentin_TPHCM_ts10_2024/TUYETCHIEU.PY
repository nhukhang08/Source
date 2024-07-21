def check_bug(arr, k):
    result = []
    check = {}
    # check = {key: index}
    for index in range(n):
        key = arr[index]
        if key in check:
            old_index = check[key] + k
            if old_index > index:
                result.append(key)           
        else:
            check[key] = index
    if len(result) == 0:
        return -1
    return min(result)
       
f, g = open("TUYETCHIEU.INP", "r"), open("TUYETCHIEU.OUT", "w")

n, k = map(int, f.readline().split())
arr = list(map(int, f.readline().split()))

g.write(str(check_bug(arr, k)))

f.close(); g.close()

