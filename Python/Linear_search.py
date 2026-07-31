# find the given target in the given list of number
def Linear_search(number,target):
    for i in range(len(number)):
        if number[i] == target:
            return i
    return -1
numbers = [10, 20, 30, 40, 50]
target = int(input("Enter the number to search: "))
result = Linear_search(numbers, target)
if result == -1:
    print("Element not found")
else:
    print("Element found at index:", result)
    