'''
Q13. Write a Python program that takes a student's score as input and
prints the corresponding grade. Use the following grading scale:

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60
'''
marks=int(input("Enter your marks out of 100:"))
if marks>=90 and marks<=100:
    print("your grade is A")
elif marks>=80 and marks<=89:
    print("your grade is B")
elif marks>=70 and marks<=79:
    print("your grade is C") 
elif marks>=60 and marks<=69:
    print("your grade is D")
elif marks<=59:
    print("your grade is F")
else:
    print("Enter a valid number!!")