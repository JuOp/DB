def num_of_words(filename):
    txt = open(filename)
    text = txt.readlines()
    for i in text:
        a = i.split()
        print(len(a))

num_of_words('input.txt')