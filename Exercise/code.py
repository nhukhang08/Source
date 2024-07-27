with open("input.txt", "r") as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))

def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a%b)

uc = ucln(arr[0], arr[-1])

with open("output.txt", "w") as file:
    file.write(str(uc) + "\n")
