#1) remove():remove the item from the list if list contain duplicate elements then remove method only
#removes 1st matching item
#2) clear():removes all items from the list
#3) index():
#create a list
my_list=[10,20,30,40,50,60]
print(my_list)

#remove():
my_list.remove(10)
print(my_list)
x=14
if x in my_list:
    my_list.remove(x)
else:
    print("item not present")

#delete keyword:(revokes)
print(my_list)
del my_list[1],my_list[3]
print(my_list)
