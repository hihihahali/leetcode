def isPalindrome(x):
    if x<0:
      return 0
    reverse = 0
    r = 0
    q = x
    while q>0:
       r = q%10
       q = int(q/10)
       reverse = reverse*10 + r
    if reverse == x:
       return True
    else:
       return False

x=121
print(isPalindrome(x))

