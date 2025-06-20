dict_words = {}
sentence = input("Text:")
words = sentence.split(' ')
words.sort()
for word in words:
    try:
        dict_words[word] += 1
    except KeyError:
        dict_words[word] = 1
