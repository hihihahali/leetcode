def check(s,k):
    n=len(s)
    sub=""
    count=0
    for i in range(0,n):
        if s[i] not in sub:
            sub=sub+s[i]
    for char in sub:
        for i in range(0,n):
            if char == s[i]:
                count=count+1
        if count%k!=0:
            return 0
    return 1
            

def x(str,k):
    count =0
    for i in range(0,len(str)-1):
        print("i=",i)
        for j in range(i+1,len(str)):   
        
                s= str[i:j+1]
                print(s)
                if check(s,k)==1:
                    count=count+1
                print("Cout=",count)
    return count

str="1020122"
print(x(str,2))

         
