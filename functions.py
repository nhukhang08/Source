def transpose(x:str) -> list:
    def backtrack(n, arr):
        if n == 1:
            result.append(''.join(arr))
        else:
            for i in range(n - 1):
                backtrack(n - 1, arr)
                if n % 2 == 0:
                    arr[i], arr[n - 1] = arr[n - 1], arr[i]
                else:
                    arr[0], arr[n - 1] = arr[n - 1], arr[0]
            backtrack(n - 1, arr)

    result = []
    arr = list(x)
    backtrack(len(arr), arr)
    return result

def is_prime(n:int) -> bool:
    if n in [2, 3]: return True
    elif n < 2 or n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0: return False
    return True
def is_square_number(n:int) -> bool:
    if int(n ** 0.5) == n ** 0.5: return True
    else: return False

def is_fibonacci(n:int) -> bool:
    if is_square_number(5*n**2 + 4) or is_square_number(5*n**2 - 4): return True
    else: return False

def nTH_fibonacci(n:int, MOD: int) -> int:
    def matrix_multiplication(a, b) -> list:
        arr = [
            [0, 0],
            [0, 0]
        ]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    arr[i][j] = ( a[i][k] * b[k][j] ) % MOD
        return arr

    def matrix_root(a):
        return matrix_multiplication(a, a)

    def binpow(a, n):
        if n == 1:
            return a
        tmp = binpow(a, n // 2)
        if n % 2 == 1:
            return matrix_multiplication(matrix_root(tmp), a)
        else:
            return matrix_root(tmp)

    fib = [
        [1, 1],
        [1, 0]
    ]
    """
    F_n+1 F_n
    F_n   F_n-1
    """
    return binpow(fib, n)[0][1]


def main():
    x = "abc"
    print( transpose(x) )

if __name__ == "__main__":
    main()