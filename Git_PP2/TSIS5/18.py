def num_of_words(filename):
    txt = open(filename)
    text = txt.readlines()
    cnt = 0
    for i in text:
        a = i.split()
        cnt += len(a)
    print(cnt)

filename = input()
num_of_words(filename)