#write a program to take input angles of the triangle and check the wether its valid or not
a1=int(input("enter angle 1:"))
a2=int(input("anter angle 2:"))
a3=int(input("enter angle 3:"))
total=a1+a2+a3
if total==180:
    print("valid triangle")
else:
    print("not a valid triangle")