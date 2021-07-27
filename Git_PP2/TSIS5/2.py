def readlines(filename, n):
    txt = open(filename)
    for i in txt.readlines():
        print(i)

n = input()
readlines('input.txt', n)