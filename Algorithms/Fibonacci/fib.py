n = int(input())

MOD = 100000000007
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

fib = [
    [1, 1],
    [1, 0]
]
print(f"So fibonacci thu {n} la: {binpow(fib, n)[0][1]}")
