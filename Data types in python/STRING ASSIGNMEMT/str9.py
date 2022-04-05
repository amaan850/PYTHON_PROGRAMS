s1 = input("enter first string")
s2 = input("enter a second string")
i = -1
s3 = ''
while True:
    i = s1.find(s2, i + 1)
    if i == -1:
        break
    j = i - 1
    if j >= 0:
        s3 += s1[j]
    j = i + len(s2)
    if j < len(s1):
        s3 += s1[j]
print(s3)
