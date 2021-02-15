def sort(a):
    l,m,h=0,0,len(a)-1
    while(m<=h):
        if a[m]==0:
            a[l],a[m] = a[m],a[l]
            l+=1
            m+=1
        elif a[m]==1:
            m+=1
        else:
            a[h],a[m] = a[m],a[h]
            h-=1
    return a

a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 
print(sort(a))
