#try:
#except:
#else:
#finally:

'''
try:
    num = int(input("please enter a number: "))
except:
    print("That's not a number!")
else:
    print("I'm in the else!")
finally:
    print("Runs no matter what!")
'''

while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("That's not a number!")
    else:
        print("Good job, you entered a number!")
        break
    finally:
        print("Runs no matter what!")

print("Rest of the game logic runs")
