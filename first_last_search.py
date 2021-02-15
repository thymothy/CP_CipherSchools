def f_search(a,st,en,x):
    if en>=st:
        mid = int(st + (en-st)/2)
        if ((mid==0 or x>a[mid-1]) and (a[mid]==x)):
            return mid
        elif a[mid]>x:
            return f_search(a,st,mid-1,x)
        else:
            return f_search(a,mid+1,en,x)
    return -1

def l_search(a,st,en,x):
    if en>=st:
        mid = int(st + (en-st)/2)
        if ((mid==n-1 or x<a[mid+1]) and (a[mid]==x)):
            return mid
        elif a[mid]>x:
            return l_search(a,st,mid-1,x)
        else:
            return l_search(a,mid+1,en,x)
    return -1


a = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(a)
x = 8
print("first " + str(f_search(a,0,n,x)))
print("second " + str(l_search(a,0,n,x)))