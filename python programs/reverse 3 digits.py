#wap to take a 3 digits number from users and print its reverse number I/P=>123
a=int(input("enter a 3 digit number"))
b=a//100
c=a%100
d=c//10
e=c%10
a=b+d*10+e*100
print(a)