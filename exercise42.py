# Define speak below:
#My solution
def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    if animal == "duck":
        return "quack"
    if animal == "cat":
        return "meow"
    if animal == "dog":
        return "woof"
    else:
        return "?"

#Official solutions
noises = {
    "dog": "woof",
    "pig": "oink",
    "duck": "quack",
    "cat": "meow"
}

def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"

#or
def speak(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')
