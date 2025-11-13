for q in range(900009, 998002) :
    if 0 == q % 11 :
        for w in range(910, 1000) :
            for e in range(990,1000) :
                if q == w * e :
                    print(q, w, e)



