def all_factors(n,i,factors):
    if i > n:
        return factors
    else:
        if n%i == 0:
            factors.append(i)
            return all_factors(n,i+1,factors)
        else:
            return all_factors(n,i+1,factors)
n = int(input())
factors = []
list_a = all_factors(n,1,factors)
print(factors)
