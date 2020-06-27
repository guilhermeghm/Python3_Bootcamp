import re

def censor(input):
    pattern = re.compile(r'((frack)[a-z]+|(frack) [a-z]+ |(frack)\b|^(frack))', re.I)
    result = pattern.sub("CENSORED", input)
    print(result)
    return result


"""
#Official solution

import re

def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", input)
"""


censor("Frack you")
censor("I hope you fracking die")
censor("you fracking Frack")
