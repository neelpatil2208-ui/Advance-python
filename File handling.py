
import re

sentence = input("Enter a sentence: ")


words = re.findall(r'\b\w+\b', sentence.lower())


duplicates = []

for word in words:
    if words.count(word) > 1 and word not in duplicates:
        duplicates.append(word)


if duplicates:
    print("Words occurring more than once:")
    for word in duplicates:
        print(word)
else:
    print("No repeated words found.")
