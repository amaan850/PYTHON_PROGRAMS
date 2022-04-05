# append():add item to the end of list
# extends():add multiple items to the list
# insert():insert an item at defined index
# 1)Append()
#create a list
my_list=[10,20,30]
print(my_list)
#Append
#add item to end of the list
my_list.append(40)
my_list.append(50)
print(my_list)

my_list.append([1,2,3])
print(my_list)
print(my_list[-1])

#extends()
#add multiple items into list
my_list.extend([89,70])
print(my_list)

#insert()
#add item to specific index
my_list.insert(1,45)
print(my_list)
my_list.insert(1,[50,59])
print(my_list)