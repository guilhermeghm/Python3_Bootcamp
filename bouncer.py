#Ask for age
age = input("How old are you: ")

#First option
#if age:
#    age = int(age)
#    if age >= 18 and age < 21:
        # 18-21 wristband
#        print("You can enter, but need a wristband")
#    elif age >= 21:
        # 21+ drink, normal entry
#        print("You are good to entter and can drink!")
#    else:
        # too young, sorry
#        print("You can't come in, little one! :(")
#else:
#    print("Plese enter an age!")


#Second option.
if age:
    age = int(age)
    if age >=  21:
        print("You are good to entter and can drink!")
    elif age >= 18:
        print("You can enter, but need a wristband")
    else:
        print("You can't come in, little one! :(")
else:
    print("Plese enter an age!")
