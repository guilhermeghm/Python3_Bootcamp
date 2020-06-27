#import re
import re

#define parse_date below
def parse_date(input):
    date_regex = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    matches = date_regex.search(input)
    if matches:
        return {
            "d": matches.group(1),
            "m": matches.group(2),
            "y": matches.group(3),
        }
    return None
