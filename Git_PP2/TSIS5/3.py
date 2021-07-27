def AppendTxt(filename, s):
    txt = open(filename, 'w')
    txt.write(s)
    print(txt.read())

s = input()
AppendTxt('input.txt', s)