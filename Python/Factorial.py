# calculate the factorial of given number
def Factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result
number = int(input("Enter the number: "))
print("Factorial:", Factorial(number)) 