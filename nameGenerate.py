import string
import random 
from collections import defaultdict


#save names in one array
with open('names.txt', 'r')as file: 
    names = file.readlines()

#divide names in characters
tokenized_names = []
for name in names:
    tokenized_name = [letter for letter in name]
    tokenized_names.append(tokenized_name)

#create default dictionary (it gives unknown key a non-zero value) of letter appearances
letter_counts = defaultdict(int)
for name in tokenized_names:
    for letter in name:
        letter_counts[letter] += 1
        
#create bigrams as tuples of adjacent letters in words
#calcuate occurences of such bigrams
bigram_counts = defaultdict(int)
for name in tokenized_names:
    for i in range(len(name) - 1):
        bigram = (name[i], name[i+1])
        bigram_counts[bigram] += 1

#count chain rule probability of next letter occuring after given letter using bigram_counts
bigram_probabilities = defaultdict(float)
for bigram, count in bigram_counts.items():
    letter1, letter2 = bigram
    bigram_probabilities[bigram] = count / letter_counts[letter1]
    
#use first letter as a starter point
#choose randomly among letters that appears in list of tuples (next_letter, possibility of its as a next letter)
#newly selected letter becomes a new starter point
#generate until next_letter candidates are found or next_letter is a '\n' character
def generateName(seed_letter):
    new_name = seed_letter
    while True:
        next_letter_candidates = []
        for bigram, probability in bigram_probabilities.items():
            if bigram[0] == seed_letter:
                next_letter_candidates.append((bigram[1], probability)) #put all bigrams starting with seed_letter (start) in one array 
        next_letter = random.choices([letter[0] for letter in next_letter_candidates],
                                      [letter[1] for letter in next_letter_candidates])[0]
        if next_letter is None:
            continue
        if not next_letter_candidates or next_letter == '\n':
            return new_name
        else:
            new_name += next_letter
            seed_letter = next_letter
            

firstLetter = input("Please provide first letter of name: ") 

print(generateName(firstLetter))

            
    

    
    

