def a(s):
    return (s+1)%2==0

f=0
for d in range(1,602001):
    if a(d):
        f=d*d+f
        print (d,d*d,f)



        
