age = 7

# 2-6 = $2/ticket
# < 65 = $5/ticket
# $10 for everyone else.

if not((age >= 2 and age <= 8) or age >= 65):
    print("You pay 10 dollars and you are not a child or senior!")
else:
    print("You are a child or senior!")
