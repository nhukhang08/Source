"""
Input: int N
Output: Là số X và những số thay đổi vị trí của X thõa mãn điều kiện
Ý tưởng: 
    Duyệt các số fib thứ tự từ 7 đến x sao cho fib[i] <= N
        Kiểm tra số nguyên tố
            Tạo hoán vị cho số
                Kiểm tra số nguyên tố
                {
                    Lưu kết quả
                }
    In kết quả

"""

MOD = 10000000000
def matrix_mul(a, b):
    arr = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                arr[i][j] += a[i][k] * b[k][j]
                arr[i][j] %= MOD
    return arr

def matrix_root(a): return matrix_mul(a, a)

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
    for i in range(5, int(x**0.5)+1, 6):
        if x % i == 0 or x % (i+2) == 0:
            return False
    return True

# def hoanvi(nums:int):
#     def backtrack(start, end):
#         if start == end:
#             value = int("".join(nums.copy()))
#             if is_prime(value) and value not in result:
#                 result.append(value)
#         if len(result) == 2:
#             return
#
#         for i in range(start, end):
#             nums[start], nums[i] = nums[i], nums[start]
#             backtrack(start + 1, end)
#             nums[start], nums[i] = nums[i], nums[start]
#
#     nums = list(str(nums))
#     result = []
#     backtrack(0, len(nums))
#
#     return result

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
            backtrack(path + options[i], options[:i] + options[i+1:])
    backtrack("", x)

    return result




f = open("NGTOFIB.INP", "r")
g = open("NGTOFIB.OUT", "w")

n = int(f.readline())

num = 0
index = 7
result = []
while num < n:
    num = binpow(fib, index)[0][1] # Fib
    if num > n:
        break
    index += 1
    # -----------------------
    if is_prime(num) and len(hoanvi(num)) == 2:
        nums = hoanvi(num)
        
        result.append(nums)

for i in range(len(result)-1):
    for j in range(1):
        g.write(str(result[i][j]) + " ")
    g.write(str(result[i][-1]) + "\n")

g.write(str(result[-1][0]) + " ")
g.write(str(result[-1][1]))

f.close(); g.close()