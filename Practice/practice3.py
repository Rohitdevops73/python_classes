# Grade student based on marks
# marks >=90 grade is A
# 90>marks >=80 grade is B
# 80> marks >=70, grade C
# 70 > marks  grade D

marks = float(input("enter you marks : "))

if (marks >= 90):
    grade = "A"
elif (marks>=80 and marks<90):
    grade = "B"
elif (marks>=70 and marks<80):
    grade = "C"
else:
    grade = "D"

print ("Your grade is -> ", grade)

