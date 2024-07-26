
def is_prime(x):
    if x in [2, 3]:
        return True
    elif x % 2 == 0 or x % 3 == 0 or x <= 1:
        return False
    for i in range(5, int(x**0.5)+1, 6):
        if x % i == 0 or x % (i+2) == 0:
            return False
    return True

print(is_prime(101))