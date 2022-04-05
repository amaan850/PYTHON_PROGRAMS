#create a list
mylist=[10,40,20,30,40,50,60,40]
print(mylist)
#index
#find the index of the given item
x= mylist.index(40)
print(x)
#....exceptional handeling.....
x=-1
while True:
    try:
        x=mylist.index(40,x+1)
        print(x)
    except:
        break
print("########################")
#count
y=mylist.count(40)
print(y)
print("######################")
x=-1
mylist=[10,40,20,30,40,50,60,40]
for i in range (y):
    x= mylist.index(40,x+1)
    print(x)