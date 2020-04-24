##MY solution
# Lists [1,2,3,4] and [3,4,5,6], only intersection.
answer = [n for n in [1,2,3,4] if n in [3,4,5,6]]
print(answer)


#List ["Elie", "Tim", "Matt"], make reversal and lower case.
answer2 = [l[::-1].lower() for l in ["Elie", "Tim", "Matt"]]
print(answer2)

##Offical solution
#Using list comprehensions:
answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]

#Without list comprehensions:
answer = []
for x in [1,2,3,4]:
    if x in [3,4,5,6]:
        answer.append(x)
answer2 = []
for name in ["Elie", "Tim", "Matt"]:
    answer2.append(name[::-1].lower())
