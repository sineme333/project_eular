def a(s):
    return s%2==0

q=0
d=0
f=1
while(d<4000000):
    g=d+f
    d=f
    f=g
    if a(d):
        q=q+d
        print(q)


