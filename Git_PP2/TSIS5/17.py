def remove_new_lines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

fname = input()
print(remove_new_lines(fname))