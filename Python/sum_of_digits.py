# sum of digits
def sum_of_digits(num):
    total = 0
    while num > 0:
        last_digits = num % 10
        total += last_digits
        num //= 10
    return total
number = int(input("enter the number :"))
print("Sum of digits of given number is :",sum_of_digits(number))