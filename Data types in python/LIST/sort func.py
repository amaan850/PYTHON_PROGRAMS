# sort function():it is used to sort the list in ascending order or desecending order by default it will
# sort list in ascending order.if we want to sort the list in descending order then we use reverse keyword
# we can also specify the custom sorting by using key attribute
#by default sorting ascending and descending and sorting
list1=[3,8,1,9,2,6]
print(list1)
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)
print("##################")
#sort by using inbuilt len
list1=['aaa','b','cc']
list1.sort(key=len)
list1.reverse()
print(list1)

#Sort by user defined function
def fun1(org):
    return arg[1]
list1=[[2,9],[5,4],[2,1]]
print(list1)
list1sort (key=fun1)
print(list1)