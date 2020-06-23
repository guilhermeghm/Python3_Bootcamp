import re

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

#print(extract_phone("My number is 432 567-8976"))
#print(extract_phone("My number is 432 567-897622"))

def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)

#print(extract_all_phones("My number is 432 567-8976 or call me at 453 445-8787"))
#print(extract_all_phones("My number is 432 567-89"))

'''
def is_valid_phone(input):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(input)
    if match:
        return True
    return False
'''

def is_valid_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False

print(is_valid_phone("434 456-3422"))
print(is_valid_phone("434 456-3422 ads"))
print(is_valid_phone("ssd 434 456-3422 d"))
