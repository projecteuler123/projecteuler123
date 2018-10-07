def sum_difference():
    s=0
    k=0
    for i in range(1,101):
        s=s+i
        k=k+i**2
        p=s**2-k
    return p
print(sum_difference())    
