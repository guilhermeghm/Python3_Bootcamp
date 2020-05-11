#My solution
def yell(phrase):
    phrase = ("{}!".format(phrase.upper()))
    return phrase

yell("go away")

#Official answers:
#Using string concatenation:
def yell(word):
    return word.upper() + "!

#Using the string format() method:
def yell(word):
    return "{}!".format(word.upper())

#Using an f-string
def yell(word):
    return f"{word.upper()}!"
