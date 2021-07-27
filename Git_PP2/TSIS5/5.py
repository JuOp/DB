def readlines(filename):
    txt = open(filename)
    list_of_lines = list(txt.readlines())
    for i in list_of_lines:
        print(i)


readlines('input.txt')