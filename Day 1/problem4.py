num=int(input('enter the number:'))
digits=0
while num!=0:
    digit=num%10
    digits=digits+1
    num=num//10
print(digits)