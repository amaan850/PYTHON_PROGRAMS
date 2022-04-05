# find():find the 1st occurence of the substring & return its index,return-1 if no string found
s1 = "this is DEMO this is first program"
x = s1.find('is')
print(x)
x = s1.find('IS')
print(x)
# index():it is similar to find function only difference is that it will generate exception if no substring is found
x = s1.index('is')
print(x)
x = s1.index('IS')
print(x)
# rindex():searches the target string for a given substring at the end raises and exception if value not found
x = s1.rindex('is')
print(x)
x = s1.rindex('IS')
print(x)
# rfind(): searches the target string for the given substring at the end and method returns -1 if the value is not found.
x = s1.rfind('is')
print(x)
x = s1.rfind('IS')
print(x)
