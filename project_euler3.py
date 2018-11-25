n=600851475143
def largeprimefactor(n):
    fact = 2
    while fact < n:
        if n % fact == 0:
            n = n / fact
            if n % fact == 0:
                n = n /fact
        fact += 1
    return fact  

print(largeprimefactor(int(n)))