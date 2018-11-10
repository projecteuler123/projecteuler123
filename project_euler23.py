
def divisor(n):
    i=2;t={1}
    l = n**0.5
    while i<=l:
        if n%i==0:
            t.add(i)
            t.add(n/i)
        i+=1
    return sum(t)

a=set()
num=set(range(28123))
for i in range(1,28123):
    if i<divisor(i):
        a.add(i)
        for j in a:
            if (i+j) in num:
                num.remove(i+j)

print(sum(num))
