def fact_sum():
    a = 100
    f = 1
    sum = 0
    for i in range(1,(a+1)):
        f = f*i
    k=str(f)
    for i in list(k):
        sum += int(i)
    print(sum)
fact_sum();