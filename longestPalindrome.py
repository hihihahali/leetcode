
def longestPalindrome(str):
    n=len(str)
    def expand(l,r):
        while l>=0 and r<=n-1 and str[l]==str[r]:
           l=l-1
           r=r+1
        return str[l+1:r]
    sub=""
    for i in range(0,n-1):
        sub1=expand(i,i)
        print("sub1=",sub1)
        if len(sub1)>len(sub):
           sub=sub1
        sub2=expand(i,i+1)
        print("sub2=",sub2) 
        if len(sub2)>len(sub):
            sub=sub2
        
    return sub       

str="babad"
haha =   longestPalindrome(str)
print(haha)     
