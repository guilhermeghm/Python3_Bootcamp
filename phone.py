import re

def extract_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

print(extract_phone("My number is 432 567-8976"))
print(extract_phone("My number is 432 567-897622"))
