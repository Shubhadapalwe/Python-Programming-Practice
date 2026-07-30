# check the given string is palindrome or not 
def Check_palindrome(s):
    reverse = ""
    for i in range(len(s)-1,-1,-1):
        reverse += s[i]
    if s == reverse:
        return True
    else:
        return False
text = input("enter the text")
print(Check_palindrome(text))