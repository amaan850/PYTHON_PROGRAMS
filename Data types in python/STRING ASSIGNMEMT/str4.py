# Given a string of even length, return the first half. So the string "CatDog" yields "Cat". If the
# string length is odd number then return null.
s1= input("enter string1:")
s2=len(s1)
s3=s2//2
if s2%2==0:
    print(s1[0:s3])
else:
    print("null")


