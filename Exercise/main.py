def CSNT_BAI1(): # https://ucode.vn/problems/bai-1-liet-ke-cac-so-nguyen-to-trong-doan-lr-156140
    L, R = map(int, f.readline().split())
    def prime(x):
        if x in [2, 3]:
            return True
        elif x < 2 or x % 2 == 0 or x % 3 == 0:
            return False
        for i in range(5, int(x**0.5)+1, 6):
            if x % i == 0 or x % (i + 2) == 0:
                return False
        return True
    arr = []
    for i in range(L, R+1):
        if prime(i):
            arr.append(i)
    g.write(str(len(arr))+ "\n")
    for i in range(len(arr)-1):
        g.write(str(arr[i])+ "\n")
    g.write(str(arr[-1]))
def CHUSO_BAI2():
    m, n, k = map(int, f.readline().split())
    t = "1"
    for i in range(n):
        if len(t) < k:
            t = str(int(t) * m)
        else:
            t = str(int(t[len(t) - k:]) * m)
    result = str(t[len(t) - k:])
    if len(result) < k:
        result = "0" * (k - len(result)) + result
    g.write(result)

def XAUCON_BAI3():
    s = f.readline()
    result = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            char = s[i:j]
            if char not in result:
                result.append(char)

    result = len(result)

    with open("output.txt", "w") as g:
        g.write(f"{result}")

def SXPS_BAI4():
    n, k = map(int, f.readline().split())
    phanso = []
    dec = []
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if i / j not in dec:
                phanso.append(f"{i}/{j}")
                dec.append(i / j)

    def sapxep(arr: int, lst: str):
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst

    result = sapxep(dec, phanso)
    g.write(result[k - 1])
def NGTOFIB_BAI5(): # https://ucode.vn/problems/bai-5-tim-so-nguyen-x-thoa-man-156139
    MOD = 10000000000
    def matrix_mul(a, b):
        arr = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    arr[i][j] += a[i][k] * b[k][j]
                    arr[i][j] %= MOD
        return arr
    def matrix_root(a):
        return matrix_mul(a, a)
    def binpow(a, n):
        if n == 1:
            return a
        tmp = binpow(a, n // 2)
        if n % 2 == 1:
            return matrix_mul(matrix_root(tmp), a)
        else:
            return matrix_root(tmp)

    fib = [[1, 1], [1, 0]]
    def is_prime(x):
        if x in [2, 3]:
            return True
        if x < 2 or x % 2 == 0 or x % 3 == 0:
            return False
        for i in range(5, int(x ** 0.5) + 1, 6):
            if x % i == 0 or x % (i + 2) == 0:
                return False
        return True
    def hoanvi(x):
        x = str(x)
        result = []
        def backtrack(path, options):
            if len(options) == 0:
                number = int(path)
                if is_prime(number) and number not in result:
                    result.append(number)
                return
            if len(result) == 2:
                return
            for i in range(len(options)):
                backtrack(path + options[i], options[:i] + options[i + 1:])
        backtrack("", x)
        return result
    n = int(f.readline())
    num = 0
    index = 7
    result = []
    while num < n:
        num = binpow(fib, index)[0][1]  # Fib
        if num > n:
            break
        index += 1
        # -----------------------
        if is_prime(num) and len(hoanvi(num)) == 2:
            nums = hoanvi(num)

            result.append(nums)
    for i in range(len(result) - 1):
        for j in range(1):
            g.write(str(result[i][j]) + " ")
        g.write(str(result[i][-1]) + "\n")
    g.write(str(result[-1][0]) + " ")
    g.write(str(result[-1][1]))
def SO_BAI6(): # https://ucode.vn/problems/bai-6-day-nhi-phan-co-dung-k-so-0-co-nghia-158499
    lines = f.readlines()
    def checkCoutZeroBinary(n, k):
        result = 0
        for i in range(1, n + 1):
            binary = bin(i)[2:]
            num0 = 0
            for num in binary:
                if num == '0':
                    num0 += 1
            if num0 == k:
                result += 1
        return result
    for line in lines:
        n, k = map(int, line.split())
        g.write(str(checkCoutZeroBinary(n, k)) + "\n")

def CHIAHET_BAI7(): # https://ucode.vn/problems/bai-7-chia-het-cho-k-158500
    m, n, k = map(int, f.readline().split())

    def checkBit(x: int):
        bit = bin(x)[2:]
        num0 = 0
        for num in bit:
            if num == "0":
                num0 += 1
        if num0 == n:
            return True
        return False

    start = int(pow(2, m + n - 1))
    end = int(pow(2, m + n)) - 1

    result = []

    for i in range(start, end + 1):
        if i % k == 0:
            if checkBit(i):
                result.append(i)

    g.write(str(len(result)) + "\n")
    for i in range(len(result) - 1):
        g.write(str(result[i]) + " ")
    g.write(str(result[-1]))

def VITRISO_BAI8(): # https://ucode.vn/problems/bai-8-tong-duong-cac-so-tren-vong-tron-158287
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

    if sum(arr) < 0:
        g.write("0")
    else:
        vitri = -1
        s = -1
        for i in range(len(arr) - 1):
            a = arr[i]
            b = arr[i + 1]

            if vitri != -1:
                s += b
                if s <= 0:
                    vitri = -1
                    s = -1
                    if a + b > 0:
                        vitri = i
                        s = a + b

            elif a + b > 0:
                vitri = i
                s = a + b

        if vitri == -1:
            g.write(str(0))
        g.write(str(vitri + 1))

def GIAITHUA_BAI9(): # https://ucode.vn/problems/bai-9-phan-tich-n-thanh-thua-so-nguyen-to-158288
    n = int(f.readline())
    def tsnt(x):
        result = []
        for i in range(2, x):
            while x % i == 0:
                result.append(i)
                x //= i
        if len(result) == 0:
            return [x]
        return result
    result = {}
    for i in range(2, n + 1):
        number = tsnt(i)
        for k in number:
            if k in result:
                result[k] += 1
            else:
                result[k] = 1
    for i, j in result.items():
        g.write(str(j) + " ")

def BHK(): # https://ucode.vn/problems/bai-10-bay-hai-khong-158559
    pass
def GOLD(): # https://ucode.vn/problems/bai-11-alibaba-va-40-ten-cuop-158504
    pass
def STRING(): # https://ucode.vn/problems/bai-12-string-158560: MPICOLY: OLYMPIC
    k = int(f.readline())
    char = f.readline()

    point = len(char) - k

    print(point)

    g.write(str(result))

f = open("input.txt", "r")
g = open("output.txt", "w")
def main():
    STRING()
    f.close(); g.close()

if __name__ == "__main__":
    main()
