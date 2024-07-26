
def eratosthenes(n):
    prime = [True for _ in range(n+1)]
    
    for p in range(2, int(n**0.5)+1):
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
    result = []
    for i in range(2, n+1):
        if prime[i]:
            result.append(i)
    return result
    

print(eratosthenes(30))
