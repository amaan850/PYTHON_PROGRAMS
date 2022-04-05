#1) split(): it is used to split string by given seperator character.
s1="This is demo"
s2="a,c,b,qwd,e,f,g"
arr=s1.split(" ")
print(arr)
for x in arr:
    print(x,len(x))
print("#############")
arr=s2.split(" ")
print(arr)
for x in arr:
    print(x)
#2) join(): this function returns the string that result from concat operation of the object in the iterable
s1="wipro"
s2=list(s1[0:2])
n=len(s1)
s2=s2*n
s3=" ".join(s2)
print(s3)