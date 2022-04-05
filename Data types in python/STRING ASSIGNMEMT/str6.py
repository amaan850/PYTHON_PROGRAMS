# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on
# the outside and the longer string on the inside. The strings will not be the same length, but they
# may be empty (length 0). If input is "hi" and "hello", then output will be "hihellohi".
s1 = input("enter string 1").lower()
s2 = input("enter string 2").lower()
n = len(s1)
n1 = len(s2)
if n1 > n:
    print(s1 + s2 + s1)
else:
    print(s2 + s1 + s2)
