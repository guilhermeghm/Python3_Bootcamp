# NO TOUCHING ======================================

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# NO TOUCHING ======================================

calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

print("Actually Sick: " +format (actually_sick))
print("Kinda Sick: "  +format (kinda_sick))
print("Hate your Job: " +format (hate_your_job))
print("Sick Days: " +format (sick_days))

if actually_sick == True and sick_days > 0:
    calling_in_sick = True
elif kinda_sick == True and hate_your_job == True and sick_days > 0:
    calling_in_sick = True
else:
    calling_in_sick = False

print("Calling in Sick: " +format (calling_in_sick))

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
