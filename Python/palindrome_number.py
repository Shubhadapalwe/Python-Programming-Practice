# check given number is palindrome or not
def check_palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        num //= 10 
    return original == reverse
number = int(input("Enter the number: "))

print("Palindrome:", check_palindrome(number))