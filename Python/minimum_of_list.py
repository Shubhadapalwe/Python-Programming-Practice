# find the minimum number from given list
def find_Minimum(number):
    min = number[0]
    for num in number:
        if num < min:
            min = num
    return min
numbers = [12, 45, 7, 9, 0]
print("Minimum element:", find_Minimum(numbers))