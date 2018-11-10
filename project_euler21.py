
def divisors(n):
    i=2;total={1}
    loop = n**0.5
    while i<=loop:
        if n%i==0:
            total.add(i)
            total.add(n/i)
        i+=1
    return sum(total)

total=0
for i in range(1,10000):
    value = divisors(i)
    if i != value and divisors(value) == i:
        total+=i
print(total)
