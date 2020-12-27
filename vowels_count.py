# To return the no. of vowels in sentence
# Assign vowels
# Collect sentence
# convert to lower case
# count vowels
# return sum of each vowel and total sum of all vowels

print("Welcome!\n Find all vowels in your sentence.")
vowels = ["a", "e", "i", "o", "u"]
user_sentence = str(input("Write your Sentence:  ")).lower()

each_vowel_count = {}

count = 0
for chr_ in ('aeiou'):
    each_count = user_sentence.count(chr_)

    each_vowel_count[chr_] = each_count
    
for chr_ in user_sentence:
    if chr_ in vowels:
        count += 1
print("Here's the total for each vowel in sentence: ", each_vowel_count, "\nHere's the total for all vowels in sentence: ", count)
