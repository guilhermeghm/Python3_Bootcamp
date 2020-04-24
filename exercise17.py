#My solution
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

result = ""

# Define your code below:
for i in sounds:
     result += (i.upper())
print(result)


#Alternative solutions
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s.upper()

#OR
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s
result = result.upper()
