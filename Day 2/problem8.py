num=int(input('enter the number:'))
reverse=0
original=num
while num!=0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if reverse==original:
 print('The number is palindrome')
else:
 print('The number is not palindrome')

