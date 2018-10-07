import math
def power_digit():
    a = 2**1000
    n=str(a)
    sum = 0
    for i in list(n):
        sum += int(i)
    print(sum)
power_digit();