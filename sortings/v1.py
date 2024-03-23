# Declare variables and arrays
# NumberList = [1,2,3,4,5,7,8,9]

NumberList = [3,2,9,7,5,1,8,4]
temp = 0

# Disply the original series
print('Before sort')
print(NumberList, end="\n\n")
print('During Sort')

# Apply sorting
for i in range(7):
    if NumberList[i] > NumberList[i+1]:
        # Swaping occurs
        temp = NumberList[i]
        NumberList[i] = NumberList[i+1]
        NumberList[i+1] = temp
    print(NumberList)
