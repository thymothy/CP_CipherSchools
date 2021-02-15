def search(a,n,x):
    i,j = 0,n-1
    while(i<n and j>0):
        if a[i][j]==x:
            return ("element found at a["+ str(i)+"]["+str(j)+"]")
        elif a[i][j]>x:
            j-=1
        else:
            i+=1
    return ("element not found")

a = [ [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50] ]
print(search(a,4,29))