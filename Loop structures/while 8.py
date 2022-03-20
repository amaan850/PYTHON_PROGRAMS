# WAP to take a  umber from user and check that number is prime or not
n = int(input("enter a number"))
f = True
i = 2
while i < n:
    if n % i == 0:
        f = False
        break
    i = i + 1
if f == True:
    print("prime")
else:
    print("not prime")
