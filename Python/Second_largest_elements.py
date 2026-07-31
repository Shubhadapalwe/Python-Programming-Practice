# find the sencond largest element 
def second_largest_element(number):
    largest = float('-inf')
    second = float('-inf')
    for num in number:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second
numbers = [12, 45, 7, 89, 34]
print("Second Largest Element:", second_largest_element(numbers))