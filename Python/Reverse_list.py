# Reverse the given list using for loop
def Reverse_list(number):
    reverse_list = []
    for i in range(len(number)-1,-1,-1):
        reverse_list.append(number[i])
    return reverse_list
numbers = [0, 9, 30, 40, 50]
print("Original List:", numbers)
print("Reversed List:", Reverse_list(numbers))