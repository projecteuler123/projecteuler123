def smallest():
    for j in range(1,250000000):
        k=0
        for i in range(2,21):
            if(j%i != 0):
                k=1
                continue
        if k==0:
            return j
print(smallest())
