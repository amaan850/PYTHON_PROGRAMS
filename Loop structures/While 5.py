# WAP to take a number from user into n and print only even numbers between 1 to n
n = int(input("enter any number"))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i = i + 1
