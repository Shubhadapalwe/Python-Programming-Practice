# sum of elements given in the array
def Sum_of_elements(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = [10, 20, 30, 80, 50]

print("Sum of list elements:", Sum_of_elements(numbers))