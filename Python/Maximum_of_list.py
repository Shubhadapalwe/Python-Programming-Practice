# find the maximum number from given list
def find_Maximum(number):
    max = number[0]
    for num in number:
        if num > max:
            max = num
    return max
numbers = [12, 45, 7, 9, 34]
print("Maximum element:", find_Maximum(numbers))