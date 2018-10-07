for i in range(1,500):
    for j in range(1,500):
        for k in range(1,500):
            a = i + j + k
            if (a == 1000) and (i**2) + (j**2) == (k**2) and i < j < k:
                print(i * j * k)
