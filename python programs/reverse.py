#wap to take 2 digit number from user and print its reverse number I/P=>89
a=int(input("enter a two digit  number"))
b=a//10
c=a%10
a=b+c*10
print(a)