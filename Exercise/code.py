f, g = open("input.txt", "r"), open("output.txt", "w")
n = int(f.readline())
def divisor(n):
    result = []
    for i in range(2, int(n**0.5)+1): # Duyệt các số từ 2 đến n**0.5
        if n % i == 0: # Kiểm tra ước
            result.append(i)
            # Kiểm tra ước đối
            if (n / i) != i:
                result.append(n // i)
    return result

def createMul(n):
    div = divisor(n)
    if len(div) == 1:
        return [div[-1], div[-1]]
    result = []
    for i in range(len(div) - 1):
        for j in range(i + 1, len(div)):

            if div[i] * div[j] == n:
                x, y = div[i], div[j]
                result.append([x, y])
    return result

def analysic(n):
    result = []
    for mul in createMul(n):
        x, y = mul
        result.append((x - 1) * (y + 1))
    return result

result = []
for num in analysic(n):
    result.append(num)

print(result)


# result.sort()
# l = len(result)
# g.write(str(l) + "\n")
#
# for line in range(l // 10):
#     for i in range(10):
#         g.write(str(result[line+i]))
#     i += 1
#     if i % 10 == 0:
#         g.write("\n")
#
# for i in range(l-1):
#     g.write(f"{result[i]} ")
# g.write(str(result[-1]))
#
#
# f.close(); g.close()
