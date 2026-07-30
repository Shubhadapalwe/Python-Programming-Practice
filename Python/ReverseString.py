def reverse_string(s):
    ans = ""
    for i in range(len(s)-1,-1,-1):
        ans += s[i]
    return ans
text = input("Enter a string: ")
print(reverse_string(text))