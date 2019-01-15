import operator
def contaParole(file):
    word_list = []
    fr = open(file, 'r')
    text = fr.read()
    fr.close
    words = text.lower().replace("\n", " ").split(" ")
    clean_up_list(words)


def clean_up_list(words):
    clean_word_list = []
    letters_and_numbers = "1234567890qwertyuiopèìasdfghjklòàùzxcvbnm"
    for word in words:
        parola = ""
        for i in range(0, len(word)):
            lettera = None
            for x in range(0, len(letters_and_numbers)):
                if (word[i] == letters_and_numbers[x]):
                    lettera = True
                    break
            if (lettera):
                parola += word[i]
        if len(parola) > 0:
            clean_word_list.append(parola)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    word_count_sorted = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        word_count_sorted = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
    count = 0
    for key, value in word_count_sorted:
        if count < 20:
            count += 1
            print(count, value, key)
        else:
            break
contaParole('sample.txt')