# don't forget to import re
import re

# define parse_bytes below:

def parse_bytes(input):
    bytes_regex = re.compile(r'\b[0-1]{8}\b')
    return bytes_regex.findall(input)


'''
#Official solution:
import re

def parse_bytes(input):
    binary_regex = re.compile(r'\b[10]{8}\b')
    results = binary_regex.findall(input)
    return results

'''
