# Given two strings, word and a separator, return a big string made of count occurrences of the
# word, separated by the separator string. if the inputs are "Wipro","X" and 3 then the output is
# "WiproXWiproXWipro".
string = input("enter string")
seperator = input("enter seperator")
count = int(input("enter occurences"))
for i in range(count):
    print(string, end='')
    if i < count - 1:
        print(seperator, end='')
