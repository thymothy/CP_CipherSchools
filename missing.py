def missing(a):
    i,total = 0,1
    for i in range(2,len(a)+2):
        total+=i
        total-=a[i-2]
    return total

print(missing([1,2,3,5,8,4,6]))
