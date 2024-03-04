def prime_num(n,i=2):
    if n == 2:
        return True
    elif n % i == 0:
        return False
    elif i * i > n:
        return True
    return prime_num(n,i+1)

def list_primes(start,end):
    list_a = []
    for j in range(start,end+1):
        is_prime = prime_num(j)
        if is_prime == True:
            list_a.append(j)
    return list_a

n1,n2 = int(input()),int(input())
print(list_primes(n1,n2))
