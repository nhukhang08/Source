def matrix_mult(A, B, mod):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]
    ]

def matrix_pow(mat, power, mod):
    result = [[1, 0], [0, 1]]  # Identity matrix
    base = mat

    while power > 0:
        if power % 2 == 1:
            result = matrix_mult(result, base, mod)
        base = matrix_mult(base, base, mod)
        power //= 2
    
    return result

def fib_matrix(n, mod):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    F = [[1, 1],
         [1, 0]]
    
    result = matrix_pow(F, n - 1, mod)
    return result[0][0]

# Ví dụ sử dụng:
n = int(input())
mod = 1000000007  # Ví dụ modulo
print(f"Số Fibonacci thứ {n} là: {fib_matrix(n, mod)}")
