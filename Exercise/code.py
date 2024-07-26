f, g = open("input.txt", "r"), open("output.txt", "w")
n = int(f.readline())
def divisor(n):
    result = []
    for i in range(1, int(n**0.5)+1): # Duyệt các số từ 2 đến n**0.5
        if n % i == 0: # Kiểm tra ước
            result.append(i)
            # Kiểm tra ước đối
            if (n / i) != i:
                result.append(n // i)
    return result

def createMul(n):
    if n == 4:
        return [[1, 4], [2, 2]]
    div = divisor(n)
    if len(div) == 1:
        return  [ [div[-1], div[-1]] ]

    result = []
    for i in range(len(div) - 1):
        for j in range(i + 1, len(div)):
            if div[i] * div[j] == n:
                x = min(div[i], div[j])
                y = max(div[i], div[j])
                result.append([x, y])
    return result

def analysic(n):
    result = []
    for mul in createMul(n):
        x, y = mul
        num = (x - 1) * (y + 1)
        result.append(num)
    return result


result = []
def processNum(arr: list):
    arr.sort(reverse=True)
    for num in arr:
        if num == 0:
            return result
        result.append(num)
    processNum(result)
    return result

arr = []
for num in analysic(n):
    if num != 0:
        arr.append(num)

def transpose(x: int):
    def backtrack(path, options):
        if len(options) == 1:
            return path
        for i in range(len(options)):
            pass

print(result)


# for num in analysic(n):
#     result.append(num)
#     while len(analysic(num)) != 0:
#         for num in analysic(num):
#             if num not in result:
#                 result.append(num)
#
# result.sort()
#

# g.write(f"{len(result)}\n")
# for i in range(0, len(result), 10):
#     g.write(" ".join(map(str, result[i:i + 10])) + "\n")

f.close(); g.close()
