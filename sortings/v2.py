# Declare variables and arrays
# NumberList = [1,2,3,4,5,7,8,9]

NumberList = [3,2,9,7,5,1,8,4]
ListSize = len(NumberList)
temp = 0

# Disply the original series
print('Before sort')
print(NumberList, end="\n\n")
print('During Sort')

# Apply sorting
for x in range(ListSize-1):
    print()
    for i in range(0,ListSize-1):
        if NumberList[i] > NumberList[i+1]:
            # Swaping occurs
            temp = NumberList[i]
            NumberList[i] = NumberList[i+1]
            NumberList[i+1] = temp
        print(NumberList)
