a=0
b=1
c=1
while True:
        a,b=b,b+a
        s=str(b)
        c=c+1
        if(len(s)==1000):
          break
          
print(c)

