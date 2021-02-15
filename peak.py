def peak(a,low,high,n):
    mid = int(low + (high-low)/2)
    if ((mid ==0 or a[mid-1]<=a[mid]) and (mid==n-1 or a[mid+1]<a[mid])):
        return mid
    elif (mid>0 and a[mid-1]>a[mid]):
        return peak(a,low,mid-1,n)
    else:
        return peak(a,mid+1,high,n)

def main(a):
    n = len(a)
    return peak(a,0,n-1,n)

a = [1, 3, 20, 4, 1, 0]
print(main(a))