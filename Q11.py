'''
Q11. A student will not be allowed to sit in exam if his/her attendance is less
than 75% 
Take following input from user

Number of classes held
Number of classes attended

1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not
'''

c_h=int(input("Enter total number of classes held:"))
c_a=int(input("Enter total number of days attended:"))
c_r= float(c_a/c_h)*100
print(f"You have {c_r} % ")
if c_r >=75:
    print("You are allowed to sit for exam")
else:
    print("You are not allowed to sit for exam")