# Given a string, if the first or last chars are 'x', return the string without those 'x' chars, and
# otherwise return the string unchanged. If the input is "xHix", then output is "Hi".
s1 = input("enter a string")
if s1[0] == 'x' and s1[-1] == 'x':
    s1 = s1[1:-1]
    print(s1)
elif s1[0] == "x":
    print(s1[1:])
elif s1[-1] == "x":
    print(s1[:-1])
else:
    print(s1)
