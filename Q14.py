'''
Q14.Write a program to calculate bill. Ask the final amount from the user.
You have to give discount and print the final bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the final amount to be paid
'''
f_a=int(input("Enter your bill amount:"))
discount=0
if f_a>=50000:
    discount=f_a-(f_a*30/100)
elif f_a>=40000 and f_a<=49999:
    discount=f_a-(f_a*25/100)
elif f_a>=30000 and f_a<=39999:
    discount=f_a-(f_a*20/100)
elif f_a>=10000 and f_a<=29999:
    discount=f_a-(f_a*10/100)
elif f_a>=1 and f_a<=9999:
    print("Sorry! No Discount")
else:
    print("Enter a valid number")

print(f"Hurray!! You pay only {discount} for your bill {f_a} ")