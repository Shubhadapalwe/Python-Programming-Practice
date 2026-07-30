#reverse the given number
def reverse_number(num):
    reverse = 0
    while num > 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        num //= 10
    return reverse
num = int(input("Enter the number: "))

print("Reverse of the given number is:", reverse_number(num))