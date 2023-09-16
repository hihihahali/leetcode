def reverse(x):
    def check(s):
        c=int(s)
        if -2**31 < c and c < 2**31 -1:
            return 1
        return 0
    s=str(x)
    if s[0]=='-':
        s=s[1:]
        s=s[::-1]
        if check(s)==1:
            s='-'+s
            return int(s)
        else:
            return 0
    else:
        s=s[::-1]
        if check(s)==1:
            return int(s)
        else:
            return 0

x=120
print(reverse(x))