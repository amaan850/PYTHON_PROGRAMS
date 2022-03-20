# Wap to take any digit from the user and print addition of 1st and last digit
n = int(input("enter a number"))
a = n % 10
while n > 0:
    b = n % 10
    n = n // 10
print(b + a)
