# check given number is armstrong number not
def check_armstrong(num):
    original = num
    total = 0
    digit = len(str(num))
    while num > 0:
        last_digit = num % 10
        total += last_digit ** digit
        num //= 10
    return original == total
number = int(input("Enter the number: "))
print("Armstrong Number:", check_armstrong(number))

