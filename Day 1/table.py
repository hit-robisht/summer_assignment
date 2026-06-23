
n=int(input('enter the value of n:'))
if n<0:
   print("factorial does not exist")
elif n==0:
   print("the factorial of 0 is 1")
else:
   i=1
   factorial=1
   while i<=n:
        factorial=factorial*i
        if i==n:
         print(factorial)
        i+=1
    