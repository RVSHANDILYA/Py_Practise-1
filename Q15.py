'''
Q15.Ask 4 numbers from user. Make sure all the numbers entered by user
are different. Print which number is the smallest.
'''
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
d=int(input("Enter 4th number:"))

small=a

if b<small:
    small=b

if c<small:
    small=c

if d<small:
    small=d

print(f"The smallest number is: {small}")