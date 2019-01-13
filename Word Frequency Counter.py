def contaParole(file):
    word_list = []
    fr = open(file, 'r')
    text = fr.read()
    fr.close
    words = text.lower().split(" ")
    for each_word in words:
        print(each_word)

contaParole('sample.txt')