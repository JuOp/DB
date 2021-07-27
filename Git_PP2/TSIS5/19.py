def chars_in_txt(fname):
    flist = open(fname).readlines()
    chars = []
    for i in flist:
        i = i.strip()
        for j in i:
            chars.append(j)
    print(chars)

fname = input()
print(chars_in_txt(fname))