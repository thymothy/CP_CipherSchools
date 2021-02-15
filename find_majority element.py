def majority(a):
    maj_index = 0
    count = 1
    n = len(a)
    for i in range(n):
        if a[maj_index] == a[i]:
            count+=1
        else:
            count-=1
        if count == 0:
            maj_index = i
            count = 1
    count = 0
    for i in range(n):
        if a[i] == a[maj_index]:
            count+=1
    if count > n/2:
        print(a[maj_index])
    else:
        print("No majority element")


majority([1, 3, 3, 1, 3, 2, 3])