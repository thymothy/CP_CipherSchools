def minplat(a,b):
    a.sort()
    b.sort()
    n  = len(a)
    pl,r,i,j=1,1,1,0
    while(i<n and j<n):
        if a[i]<=b[j]:
            pl+=1
            i+=1
        elif a[i]>b[j]:
            pl-=1
            j+=1
    r = max(r,pl)
    return r


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)
 
print("Minimum Number of Platforms Required = ",
      minplat(arr, dep))