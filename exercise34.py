#My answer
vowels = ["a","e","i","o","u"]

answer = dict.fromkeys(vowels, 0)
print(answer)

#Official solutions
answer = {char:0 for char in 'aeiou'}

#Or
answer = dict.fromkeys("aeiou", 0)
