def intToRoman(num:int):
    symbol = [['I',1],['V',5],['X',10],['L',50],['C',100],['D',500],['M',1000]]
    if num <=0 and num >3999:
        return None
    def convert(x):
        a=[]
        for i in range(0,len(symbol)):
            if x>symbol[i][1]:
                a.append(symbol[i])
            elif x==symbol[i][1]:
                return symbol[i][0]
            else:
                a.append(symbol[i])
                break
        roman=""
        i=len(a)-2
        while i>=0:
            if a[-1][1] - a[i][1] == x:
                roman = a[i][0] + a[-1][0]
                return roman
            else:
                i=i-1
        k=len(a)-1
        y=x
        while y>0 and k>=0:
            if y >= a[k][1]:
                y=y-a[k][1]
                roman = roman + a[k][0]
            else:
                k=k-1
        return roman
    str = []
    q=num
    k=1
    while q>0:
        x = q%10*k
        str.append(convert(x))
        q=int(q/10)
        k=k*10
    result = ""
    for i in range(len(str)-1,-1,-1):
        result = result + str[i]
    return result
    
num=1994
print(intToRoman(num))
