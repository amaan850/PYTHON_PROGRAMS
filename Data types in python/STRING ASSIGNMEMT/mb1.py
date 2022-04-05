from math import sqrt
while True:
    num = int(input())
    if num == 0:
        break
    div = sqrt(num)
    if div == int(div):
        print("yes")
    else:
        print("no")
