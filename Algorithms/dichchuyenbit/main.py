def left_shift(arr, k):
    k = k % len(arr)
    return arr[k:] + arr[:k]

def right_shift(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

# Đọc đầu vào
n = int(input())
arr = list(map(int, input().split()))
t = int(input())

for _ in range(t):
    s = input().strip()
    if s.startswith("<<"):
        x = int(s[2:])
        arr = left_shift(arr, x)
    elif s.startswith(">>"):
        x = int(s[2:])
        arr = right_shift(arr, x)
    print(*arr)
'''
INPUT:
5
1 2 3 4 5
2
<<4
>>1
OUTPUT:
5 1 2 3 4
4 5 1 2 3
'''