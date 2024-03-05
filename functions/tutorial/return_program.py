# initalization of variables
payment = 0
tip_payment = 0
total = 0
# define a function called `calculate_tip`

payment = int(input("Enter the total value: ")) # ask the user for the total payment

def calculate_tip() -> tuple:
    """
    The function `calculate_tip` is used to calculate the tip for a variable that is a parameters:
    - `payment` : A variable that contains the total payment before tips, it is of the data type int
    """
    tip_payment = payment * 0.10 # calculate the tip payment 
    total = payment + tip_payment # calculate the total amount
    return (total, tip_payment)

total, tip_payment = calculate_tip()

print(f"Tip Payment is : {tip_payment}") # Display the tip payment to the user
print(f"Total payment is : {total}") # Display the total payment to the user

