#write a program that will check whether given string is pallindrome or not
s1=input("enter a string")
s2=s1[::-1]
if s1==s2:
    print("pallindrome")
else:
    print("not a pallindrome")