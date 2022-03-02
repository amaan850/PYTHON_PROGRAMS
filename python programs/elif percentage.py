#wap to input marks of 5 subjects physics,chemistry,biology,Mathematics and computer.calculate percentage and grade
#accordingly to following:
# percentage>=90%: Grade A
# percentage>=80%: Grade B
# percentage>=70%: Grade C
# percentage>=60%: Grade D
# percentage>=40%: Grade E
# percentage <40%: Grade F
m1=int(input("enter subject marks"))
m2=int(input("enter subject marks"))
m3=int(input("enter subject marks"))
m4=int(input("enter subject marks"))
m5=int(input("enter subject marks"))
total= m1+m2+m3+m4+m5
per=total*0.2
if per>=90:
    print("GRADE A")
elif per>=80:
    print("GRADE B")
elif per>=70:
    print("GRADE C")
elif per>=60:
    print("GRADE D")
elif per>=40:
    print("GRADE E")
else:
    print("GRADE F")


