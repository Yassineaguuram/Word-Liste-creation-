import itertools
#add name 
words = ['Name']

# Generate numbers from 0000 to 9999
numbers = ['{:04d}'.format(i) for i in range(10000)]

# Combine words with numbers
word_list = [word + number for word, number in itertools.product(words, numbers)]

# Add variations
word_list.extend([word.lower() + number for word, number in itertools.product(words, numbers)])
word_list.extend([word.upper() + number for word, number in itertools.product(words, numbers)])
word_list.extend([word.capitalize() + number for word, number in itertools.product(words, numbers)])

# Save the word list to a file
with open("word_list.txt", "w") as file:
    for word in word_list:
        file.write(word + '\n')

print("Word list created and saved to word_list.txt.")
