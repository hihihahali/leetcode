def x(arr):
    mod=10**9+7
    print(mod)
    index = 0
    c=0
    for i in range(0,len(arr)-1):
        a=arr[i]**arr[i+1]
        print(a)
        if a < mod:
             b=a
        else:
             b=a%mod
        if b>c:
             c=b
             index = i+1
    return index
arr=[1,2,3]
print(x(arr))
