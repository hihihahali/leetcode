def candy(rating):
   n = len(rating)
   candy = []
   for i in range(0,n):
      candy.append(1)
   print(candy)
   for i in range(n-1,0,-1):
      if rating[i] < rating[i-1]:
         if candy[i-1] <= candy[i]:
             candy[i-1] = candy[i] + 1
   print(candy)
   for i in range(1,n):
      if rating[i] > rating[i-1]:
         if candy[i] <= candy[i-1]:
             candy[i] = candy[i-1] + 1
   print(candy)
   return sum(candy)
     
rating = [1,6,10,8,7,3,2]
b = candy(rating)
print(b)