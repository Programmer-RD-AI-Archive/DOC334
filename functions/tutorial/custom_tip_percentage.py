# initalization of variables
payment = 0
tip_payment = 0
total = 0
# define a function called `calculate_tip`

def calculate_tip(payment:int,tip_payment:float = 0.10) -> tuple:
    """
    The function `calculate_tip` is used to calculate the tip for a variable that is a parameters:
    - `payment` : A variable that contains the total payment before tips, it is of the data type int
    The function returns of data type `tuple` which contains 2 elements : (total, tip_payment)
    """
    return payment * tip_payment # calculate the tip payment 

payment = int(input("Enter the total value: ")) # ask the user for the total payment
tip_payment = float(input("Please enter the percentage of the tip u would like to give: ")) / 100
tip_payment = calculate_tip(payment, tip_payment)
total = payment + tip_payment # calculate the total amount

print(f"Tip Payment is : {tip_payment}") # Display the tip payment to the user
print(f"Total payment is : {total}") # Display the total payment to the user

