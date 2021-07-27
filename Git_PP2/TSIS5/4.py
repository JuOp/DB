def read_last_lines(filename, n):
    txt = open(filename)
    a = txt.readlines()
    b = len(a)
    c = a[b-1-n:-1]
    print(c)

n = input()
read_last_lines('input.txt', n)