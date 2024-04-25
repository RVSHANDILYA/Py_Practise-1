'''
Q12.Write a program to check if number is divisible by 2 and 3 but not 8.
'''
num=int(input("Enter a number:"))
if num%2==0 and num%3==0 and num%8!=0:
    print(f"The num {num} is divisible by 2 and 3 but not 8")
else:
    print(f"doesn't meet condition")