def a(s):
    return s%3==0 or s%5==0

d=0
for f in range(10):
    if a(f):
        d=d+f
        print(d) 

print (d)