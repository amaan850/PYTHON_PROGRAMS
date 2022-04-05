#given two strings,append them together("known as concatination")
# and return the result .however if the concatination creates a
#double-char,then omit one of the chars.
#if the inputs are "Mark" and "kate" then the output should be "Markate"
#The output should be in lowercase.
s1= input("eneter string: ").lower()
s2= input("enter string 2:").lower()
s3=""
if s1[-1]==s2[0]:
    s3= s1+s2[1:]
else:
    s3=s1+s2
print(s3)