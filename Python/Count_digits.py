#Problem: Count Digits in a Number
def count_dgits(num):
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    return count
number = int(input("Enter the number: "))
print("no of digits : ",count_dgits(number))
