##My solution
#String amazing, new list with all letters Without vowels.
word = "amazing"
answer = [l for l in word if l not in ["a","e","i","o","u"]]
print(answer)


#Offical solution
#Using a string (preferable solution):
answer = [char for char in "amazing" if char not in "aeiou"]

#Using a list:
answer = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]]
