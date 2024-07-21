import math

a, b = map(int, input().split())

# Giai thừa
fatorial = math.factorial(a)

# Tổ hợp: 
comb = math.comb(a, b) # (n, k)

# BCNN, UCLN
bcnn = math.lcm(a,b)
ucln = math.gcd(a,b)




