##My example
#List ["Elie", "Tim", "Matt"]
list1 = ["Elie", "Tim", "Matt"]
answer = [n[0] for n in (list1)]
print(answer)

#List [1,2,3,4,5,6]
list2 = [1,2,3,4,5,6]
answer2 = [num for num in list2 if num %2 == 0]
print(answer2)


##Offical solution
#Using list comprehensions:
answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]

#Using manual loops:
answer = []
for person in ["Elie", "Tim", "Matt"]:
    answer.append(person[0])
answer2 = []
for num in [1,2,3,4,5,6]:
    if num % 2 == 0:
        answer2.append(num)
