#WAP  to take character from user & check that character is capital letter,small case letter and digit
a=ord(input("enter char:"))
if a>=65 and a<=90:
    print("Capital")
elif a>=97 and a<=122:
    print("small")
elif a>=48 and a<=57:
    print("digit")
else:
    print("idk this char")
