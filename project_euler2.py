def fib_sum():
    first = 1
    last = 2
    c = first + last
    s=[]
    while first < 4000000:
        first = last
        last = c
        c = first + last
        if first % 2 == 0:
            s.append(first)
    return s    
print(sum(fib_sum()))        
