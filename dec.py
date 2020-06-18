def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
        print("")
    return wrapper

@be_polite
def greet():
    print("My name is Colt.")

@be_polite
def rage():
    print("I hate you!")

#We are decorating our function
#With politeness!

'''
#Without decorator

greet = be_polite(greet)
greet()

polite_rage = be_polite(rage)
polite_rage()
'''

greet()
rage()
