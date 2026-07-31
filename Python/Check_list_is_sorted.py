# Check the given list is sorted or not
def check_list_is_sorted(number):
    for i in range(len(number)-1):
        if number[i] > number[i+1]:
            return False
    return True
numbers = [10, 20, 30, 40, 50]
print("Is the list sorted?", check_list_is_sorted(numbers))