import math
l=set()
c=0
for i in range(2,101):
    for j in range(2,101):
        l.add(i**j)
for k in l:
    c=c+1
print(c)