'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

#MY solution
#return string.lower().count(letter.lower())
def is_palindrome(string):
    string = string.lower().replace(" ", "")
    if string == string[::-1]:
        return True
    else:
        return False

#Official solution
def is_palindrome(string):
    return string == string[::-1]

#Or
def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]
