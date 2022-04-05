# lstrip():remove white space from left side
# rstrip():remove the white space from the right side
# rstrip():remove white spaces from both sides(comment each one seperatley and then run)
s1="---hello---"
print(len(s1))
s1=s1.lstrip('-')
print(s1)
print(len(s1))

s1=s1.rstrip('-')
print(s1)
print(len(s1))

s1=s1.strip('-')
print(s1)
print(len(s1))
