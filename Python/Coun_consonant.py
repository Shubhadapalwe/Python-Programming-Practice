#Write a function to count the number of consonants in a given string.
def count_consonant(s):
    count = 0
    vowels = "aeiou"
    for ch in s.lower():
        if ch.isalpha() and ch not in vowels:
            count = count + 1
    return count
text = input("enter the string")
print("number of consonants",count_consonant(text))
