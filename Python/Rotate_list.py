# rotate the given list 
def Rotate_list(number):
    last = number[-1]
    for i in range(len(number)-1,0,-1):
        number[i] = number[i-1]
    number[0] = last
    return number


numbers = [10, 20, 30, 40, 50]

print("Rotated Array:", Rotate_list(numbers))