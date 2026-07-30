#Problem: Count Vowels in a String
#Problem Statement: Write a function that counts the number of vowels (a, e, i, o, u) in a given string
def Vowels_count(s):
    count = 0
    vowels = 'aeiouAEIOU'
    for ch in s:
        if ch in vowels:
            count += 1
    return count

text = input("Enter a string: ")
print("Number of vowels:", Vowels_count(text))

        