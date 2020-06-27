import re

text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"
pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) [a-z]+', re.I)

#Option 1
result = pattern.sub("REDACTED", text)
print(result)

#Option 2
result2 = pattern.sub("\g<1> REDACTED", text)
print(result2)

#Option3
pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+', re.I)
result3 = pattern.sub("\g<1> \g<2>", text)
print(result3)
