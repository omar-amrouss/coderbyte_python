# Using the Python language, have the function Palindrome(str) take the str parameter being passed 
# and return the string true if the parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. 
# For example: "racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string. 

def Palindrome(str):
    str = str.replace(" ", "")
    ls = list(str)
    rev = reversed(ls)
    if ''.join(rev) == str:
        return "true" 
    return "false"
print(Palindrome("etetete"))
