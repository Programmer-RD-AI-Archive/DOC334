import math # importing the variable `math

# initialization of variables
num_1, num_2, operator, msg_1, msg_2 = 0, 0, "", "Enter number 1: ", "Enter number 2: "
# creating a dictionary that contains the basic operations which dont require an specific function of their own
basic_operations = {
    "+": lambda val_1, val_2: val_1 + val_2,
    "-": lambda val_1, val_2: val_1 - val_2,
    "*": lambda val_1, val_2: val_1 * val_2,
    "/": lambda val_1, val_2: val_1 / val_2,
}


def power(base: float, power: float) -> float:
    """
    The operation of the power of a number based on user inputs occurs

    The function takes in 2 parameters: `base` and `power` (both of data type float)
    - `Power` is the power value of the return value
    - `base` is the base value of the return value
    The function returns a value which is of data type float
    """
    return math.pow(base, power)


operator = str(input("Enter operator: "))
if operator == "^":
    msg_1, msg_2 = "Enter the base number: ", "Enter the power value: "
num_1 = float(input(msg_1))
num_2 = float(input(msg_2))

if operator == "^":
    result = power(num_1, num_2)
elif operator in basic_operations:
    result = basic_operations[operator](num_1, num_2)
else:
    result = "INVALID OPERATION!"
print(f"{num_1} {operator} {num_2} = {result}")
