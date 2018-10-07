import math
import sys
def Divisors(a):
    divisorsList = []
    b = 1
    while b <= math.sqrt(a):
        if a % b == 0:
            divisorsList.append(b)
            divisorsList.append(int(a / b))
        b += 1
    return divisorsList

def sum(n):
    summary = (n * (n +1)) / 2
    return int(summary)


for i in range (sys.maxsize**10):
    if len(Divisors(sum(i))) >= 500:
        print(sum(i))
        break
