def addTowNumbers(l1,l2):
    l3=[]
    miss=0
    if len(l1) == len(l2):
        for i in range(0, len(l1)):
            l2[i] = l2[i] + miss
            sum = (l1[i]+l2[i])
            if sum >= 10:
                sum = sum - 10
                if i == len(l1)-1:
                    l3.insert(i+1,1)
                l3.insert(i,sum)
                miss = 1
            else:
                l3.insert(i,sum)
                miss = 0
        return l3
    a = l1
    b = l2
    if len(l1) < len(l2):
        l1=b
        l2=a

    for i in range(0, len(l2)):
        l2[i] = l2[i] + miss
        sum = (l1[i]+l2[i])
        if sum >= 10:
            sum = sum - 10
            l3.insert(i,sum)
            miss = 1
        else:
            l3.insert(i,sum)
            miss = 0
    for i in range(len(l2),len(l1)):
        l2.append(0)
        l2[i] = l2[i] + miss
        sum = (l1[i]+l2[i])
        if sum >= 10:
            sum = sum - 10
            if i == len(l1)-1:
                l3.insert(i+1,1)
            l3.insert(i,sum)
            miss = 1
        else:
            l3.insert(i,sum)
            miss = 0
    return l3
x=[9,9,9,9,9,9,9]
y=[9,9,9,9]
b = addTowNumbers(x,y)
print(b)