def word_count(sentence):
    words = sentence.split()
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    return len(words), word_frequency

# Test the function
sentence = input("Enter a sentence: ")
count, frequency = word_count(sentence)
print(f"The number of words in the sentence is: {count}")
print("Word frequencies:")
for word, freq in frequency.items():
    print(f"{word}: {freq}")

