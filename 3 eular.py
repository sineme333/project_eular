def a(s) :
    e = True
    for q in range(2, int(s**0.5)+1) :
        if s % q == 0 :
            e = False
            break
    return e
        
for w in range (1, int(600851475143**0.5)+1) :
    if a(w) :
        if 600851475143 % w == 0 :
            print ("true", w)
