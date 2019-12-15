word_number = int(input())
word_list = []
for item in range(word_number):
    word = input()
    if len(word) > 10:
        tmp = (word[0] + str(len(word)-2) + word[-1])
        word_list.append(tmp)
    else:
        word_list.append(word)
for item in word_list:
    print(item)
