# Wap to take any digit from user and print addition of its digit
n = int(input("enter a number:"))
sum = 0
while n > 0:
    b = n % 10
    sum = sum + b
    n = n // 10
print(sum)
