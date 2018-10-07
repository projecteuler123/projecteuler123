def prime():
    l=[2,3,5,7,11,13]
    for i in range(8,1000):
        if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0 and i%13!=0:
            l.append(i);
    return l[11]
print(prime())   
