def sum(a):
    m,ms=0,0

    for i in range(len(a)):
        m+=a[i]
        if m>ms:
            ms=m
        if m<0:
            m=0
    return ms
    
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sum(a))