def find(a):
    st,en = 0,len(a)-1
    while st<en:
        while a[st]==0 and st<en:
            st+=1
        while a[en]==1 and st<en:
            en-=1
        while st<en:
            a[st]=0
            a[en]=1
            st+=1
            en-=1
    return a

a = [0, 1, 0, 1, 1, 1] 
print(find(a))