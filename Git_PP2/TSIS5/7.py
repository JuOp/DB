def readlines(filename):
    txt = open(filename)
    text = []
    a = txt.readlines()
    for i in a:
        text.append(i)
    print(text)

readlines('input.txt')