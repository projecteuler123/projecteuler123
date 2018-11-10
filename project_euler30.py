def sum_fifth():
    l = []
    c = 0
    k = 0
    for i in range(999999):
        sum = 0
        j = i
        while (i > 9):
            sum += (i % 10)**5
            i = int(i / 10)
        sum+=i**5
        if sum == j:
            l.append(j)
            c = c + 1
    for i in range(0,c):   
        k += l[i]
    print(k-1)
sum_fifth();
 