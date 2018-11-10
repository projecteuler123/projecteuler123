def digit():
    f=[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    s=0
    for n in range(3,100000):
        if n==sum( f[int(d)] for d in str(n) ):
            s+=n
    return s
print(digit())

