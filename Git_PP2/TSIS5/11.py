def size_of_file(filename):
    txt = open(filename)
    a = txt.read()
    b = a.__sizeof__
    print(b)

size_of_file('input.txt')