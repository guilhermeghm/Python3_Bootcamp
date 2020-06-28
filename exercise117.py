'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''

def truncate(string, number):
    if number < 3:
        return "Truncation must be at least 3 characters."
    if  len(string) < number:
        return string
    else:
        number -= 3
        return string[:number] + '...'

print(truncate("Super cool", 2))
print(truncate("Yo",100))
print(truncate("Another test", 12))
