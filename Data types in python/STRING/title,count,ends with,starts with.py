# title():return a string in which the 1st character of each word convert into upper case & ramining letters are lower case
s1 = "this is DEMO.this is first program"
print(s1.title())
# count():count the no of occurence of the substring
x= s1.count('is')
print(x)
# ends with(): returns tru if the string ends with the substring
print(s1.endswith("m"))
print(s1.endswith("ram"))
print(s1.endswith('gram'))
print(s1.endswith('pro'))
# starts with(): return true is string start with substring
print(s1.startswith('th'))
print(s1.startswith('this'))
print(s1.startswith('is'))
