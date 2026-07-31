# Remove duplicate from given list
def Remove_duplicate(number):
    unique = [number[0]]
    for i in range(1,len(number)):
        if number[i] != unique[-1]:
            unique.append (number[i])
    return unique
numbers = [1, 1, 1, 1, 3, 4, 4, 5,6]

print("List after removing duplicates:", Remove_duplicate(numbers))