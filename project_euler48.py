def self_power():
    sum = 0
    l = []
    for i in range(1,1001):
        sum = sum + i**i
    a = str(sum)
    c = len(a)-10
    print(a[c:])
self_power()