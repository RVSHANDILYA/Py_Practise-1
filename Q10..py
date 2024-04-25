'''
Q10. Write a program that takes two numbers as input and checks if the first
number is divisible by the second.
'''
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd Number:"))
if a%b==0:
    print(f"{a} is divisible by {b}")
else:
    print(f"{a} is not divisible by {b}")