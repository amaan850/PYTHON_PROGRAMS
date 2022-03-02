#write a program to take 3 digit number from user and check that number is armstrong number or not i/p=>153
a=int(input("enter any number"))
b=a//100
c=a%100
d=c//10
e=c%10
f=b**3+d**3+e**3
if f==a:
    print("armstrong number")
else:
    print("not armstrong number")