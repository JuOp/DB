import re
a = input()
b = input()
b1 = len(b)
cnt=0
d = False
while b1<len(a):
    c = re.search(b, a)
    if c:
        print('(', c.start()+cnt, ', ', c.end()-1+cnt, ')', sep='')
        x = int(c.start())
        a = a[x+1:]
        cnt=cnt+x+1
        d = True
    else:
        a = a[1:]
if d == False:
    print('(-1, -1)')