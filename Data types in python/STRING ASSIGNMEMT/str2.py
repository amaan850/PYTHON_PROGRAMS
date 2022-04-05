# given a string,return a new string made of n copies of the first 2 chars of the original string
# where n is the length of the string .the string maybe any length.if there are fewer than 2 chars,use
# whatever is there.if input is "wipro" then output should be wi wi wi wi wi
s1 = 'wipro'
n = len(s1)
print(n)
s2 = " "
i = 0
while i < n:
    s2 = s2 + s1[0:2]
    i = i + 1
print(s2)
