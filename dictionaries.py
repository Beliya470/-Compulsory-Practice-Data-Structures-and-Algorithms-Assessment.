import re

def word_frequency(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
