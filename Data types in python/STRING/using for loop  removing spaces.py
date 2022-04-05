s1 = "   Hello world   "
s2 = ""
j = 0
for i in range(len(s1)):
    if s1[i] != ' ':
        break
j = i
for i in range(len(s1) - 1, -1, -1):
    if s1[i] != ' ':
        break
    s2 = s1[j:i]
print(len(s2))
print(s2)
