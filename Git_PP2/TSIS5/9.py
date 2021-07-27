def num_of_lines(filename):
    txt = open(filename)
    text = txt.readlines()
    print(len(text))


num_of_lines('input.txt')