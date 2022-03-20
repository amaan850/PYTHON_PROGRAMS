# WAP to take a number from user into n and add all numbers between 1 to n
n = int(input("enter a number"))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1
    print("sum is", sum)
