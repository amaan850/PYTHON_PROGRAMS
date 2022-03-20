# WAP to take a number from user and print its factorial value
n = int(input("enter a number"))
i = 1
sum = 1
while i <= n:
    sum = sum * i
    i = i + 1
    print("sum is", sum)
