word_number = int(input('number of word: '))
words_list = []
short_words = []
for item in range(word_number):
    word = input('words: ')
    if len(word) >= 10:
        words_list.append(word)
    else:
        short_words.append(word)
for words in short_words:
    print(words)
for words in words_list:
    print(words[0] + str(len(words)) + words[-1])