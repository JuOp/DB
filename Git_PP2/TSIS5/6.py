def readlines(filename):
    txt = open(filename)
    text = list(txt.readlines())
    for i in text:
        print(i)


readlines('input.txt')