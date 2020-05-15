'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

#My solution:
def capitalize(string):
    return string[0].upper() + string[1:]

#Official solution:
def capitalize(string):
    return string[:1].upper() + string[1:]
