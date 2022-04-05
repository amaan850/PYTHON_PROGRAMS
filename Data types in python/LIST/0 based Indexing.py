#By using 0 based indexing:the index of the 1st element is 0 index of the last element is size -1
my_list=[10,20,30,1.2,'abc']
print(my_list)
my_list[0]
print(my_list[0])
my_list[3]
print(my_list[3])
#creating a list
my_list=[10,20,30,1.2,'abc']
print(type(my_list))
#get item present at 0 index
print(my_list[0])
#find size of list
print(len(my_list))
#display all items from list using for loop
print("**********")
for i in range(len(my_list)):
    print(my_list[i])
#Display all items from list using for each loop
print("*******")
for x in my_list:
    print(x)