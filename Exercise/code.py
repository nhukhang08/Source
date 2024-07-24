f, g = open("input.txt", "r"), open("output.txt", "w")
n = int(f.readline())

def ONES(n: int): # https://ucode.vn/problems/bai-17-so-mot-159012
    result = [str(num) for num in range(1, n)] + [str(n)] + [str(num) for num in range(n - 1, 0, -1)]
    return "".join(result)

g.write(ONES(n))

num = int("1" * n)

print(num**2)



f.close; g.close()