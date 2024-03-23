import csv

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # Changed the comparison for descending order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def read_numbers_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        numbers = [int(num) for row in reader for num in row]
    return numbers

def write_numbers_to_csv(numbers, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(numbers)

input_file = "input.csv"
output_file = "output.csv"

# Read numbers from input CSV file
numbers = read_numbers_from_csv(input_file)

# Sort numbers in descending order using bubble sort
bubble_sort_descending(numbers)

# Write sorted numbers to output CSV file
write_numbers_to_csv(numbers, output_file)

print("Numbers have been sorted in descending order and written to", output_file)


