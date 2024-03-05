# initalization of variables
payment = 0
tip_payment = 0
total = 0
# define a function called `calculate_tip`
payment = int(input("Enter the total value: ")) # ask the user for the total payment

def calculate_tip():
    tip_payment = payment * 0.10 # calculate the tip payment 
    total = payment + tip_payment # calculate the total amount
    print(f"Tip Payment is : {tip_payment}") # Display the tip payment to the user
    print(f"Total payment is : {total}") # Display the total payment to the user

calculate_tip()
