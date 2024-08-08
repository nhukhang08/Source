def div(n):
    result = []
    for i in range(1, int(n**0.5)+1):

        if n % i == 0:
            result.append(i)
            if (n / i) != i:
                result.append(n//i)
    return result

print(div(120))
