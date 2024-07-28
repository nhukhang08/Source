with open("input.txt", "r") as f:
    s = f.readline()
    a, b = map(int, f.readline().split())


def base_a_to_decimal(s, a):
    return int(s, a)

def decimal_to_base_b(n, b):
    if n == 0:
        return 0
    result = ""
    while n != 0:
        result += str(n % b)
        n //= b
    
    result = result[::-1]
    
    for i in range(len(result)):
        if result[i] == 
    



with open("output.txt", "w") as g:
    g.write(str(dec))