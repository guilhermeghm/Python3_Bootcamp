#Doing in a way that you don't know the position (My solution).
# DON'T TOUCH THIS PLEASE!
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!

#Change "Hanna" to "Hannah"
for n, i in enumerate(people):
    if i == "Hanna":
        people[n] = "Hannah"

#Change "Geoffrey" to "Jeffrey"
for n, i in enumerate(people):
    if i == "Geoffrey":
        people[n] = "Jeffrey"

#Change "aparna" to "Aparna" (capitalize it)
for n, i in enumerate(people):
    if i == "aparna":
        people[n] = "Aparna"

print(people)



#Doing in a way that you know the position (Official solution).
# DON'T TOUCH THIS PLEASE!
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!
#Change "Hanna" to "Hanna"
people[0] = "Hannah"
#Change "Geoffrey" to "Jeffrey"
people[4] = "Jeffrey"
#Change "aparna" to "Aparna" (capitalize it)
people[-1] = "Aparna"
