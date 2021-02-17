h = ["", "", "abc", "def", "ghi", "jkl","mno", "pqrs", "tuv", "wxyz"]

def oldphone(a,i,b,n):
    if i==n:
        print(b)
        return
    for j in range(len(h[a[i]])):
        b.append(h[a[i]][j])
        oldphone(a,i+1,b,n)
        b.pop()
        if(a[i]==0 or a[i]==1):
            return

a = [2,3,4]
oldphone(a,0,[],3)