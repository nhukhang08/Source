def is_prime(n):
    if n in [2, 3]:
        return True
    elif n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

with open("input.txt", "r") as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

def find_max(arr):
    check = 0
    max_value = 0
    index = -1
    for i in range(len(arr)):
        if int(str(arr[i])[0]) > check:
            check = int(str(arr[i])[0])
            max_value = arr[i]
            index = i
    return max_value, index

result = ""
for i in range(n):
    max_value, index = find_max(arr)
    arr.pop(index)
    result += str(max_value)

print(result)




# with open("output.txt", "w") as g:
#     g.write()
