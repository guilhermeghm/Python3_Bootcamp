'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#My solution:
#define single_letter_count below:
def single_letter_count(word,letter):
    word = word.lower()
    letter = letter.lower()
    count = 0
    for i in word:
        if i == letter:
            count += 1
    return count


#Official answer:
def single_letter_count(string,letter):
    return string.lower().count(letter.lower())
