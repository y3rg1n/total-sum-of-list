def sum_list(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total

numbers = input("Input list of numbers to sum up, separated by spaces:")
numbers = list(map(float, numbers.split()))
print("Total is:", sum_list(numbers))