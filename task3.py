# task 3

import re

#reading data
f = open('about.txt', 'r')
data = f.read()
f.close()


# regular expression pattern for a word
pattern = "[a-zA-Z]+"


# extracting all words from text
words = re.findall(pattern,data)

wordsWithAtleastSixLetters = []
for i in words:
  if len(i) >= 6:
    wordsWithAtleastSixLetters.append(i)


print("Words with atleast six letters are:")
for i in wordsWithAtleastSixLetters:
  print(i)
print()


frequency = dict()
for i in words:
  if i in frequency:
    frequency[i] += 1
  else:
    frequency[i] = 1

mostFrequent = ""
countOfMostFrequent = 0

for word in frequency:
  if frequency[word] > countOfMostFrequent:
    mostFrequent = word
    countOfMostFrequent = frequency[word]

print("The most frequently used word is:", mostFrequent)