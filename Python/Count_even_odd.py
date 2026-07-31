# count the even and odd number from given list
def count_even_odd(numbers):
    even = 0
    odd = 0
    for num in numbers:
        if num % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return even , odd
numbers = [10, 2, 6, 21, 6, 7]
even, odd = count_even_odd(numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)