def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = file.readline().strip().split()
        numbers = [int(num) for num in numbers]
    return numbers

def write_numbers_to_file(numbers, filename):
    with open(filename, 'w') as file:
        for num in numbers:
            file.write(str(num) + ' ')

input_file = "input.txt"
output_file = "output.txt"

# Read numbers from input file
numbers = read_numbers_from_file(input_file)

# Sort numbers using bubble sort
bubble_sort(numbers)

# Write sorted numbers to output file
write_numbers_to_file(numbers, output_file)

print("Numbers have been sorted and written to", output_file)
