def shares(a):
    if (len(a) == 0):
        return 0
    c,mc=0,0
    mp = a[0]
 
    for i in range(len(a)):
        mp = min(mp, a[i])
        c = a[i] - mp
        mc = max(mc,c)
    return mc
 

prices = [ 7, 1, 5, 3, 6, 4 ]

print(shares(prices))



