import time

start = time.perf_counter()

def fib(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]



print(fib(1000000))

end = time.perf_counter()

print(end - start)