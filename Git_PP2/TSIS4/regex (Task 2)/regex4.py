import re
a = input()
b = re.findall('\B[euioaAOIUE]{2,}\B', a)
b1 = len(b)
c = re.findall('[euioaAOIUE]{2,}', a)
c1 = len(c)
for i in range(0, b1):
    if i==0:
        x=c[0]
        x=x[1:]
        if b[i]!=x:
            print(b[i])
    elif i==b1-1:
        z=c[c1-1]
        z=z[:-1]
        if b[i]!=z:
            print(b[i])
    else:
        print(b[i])

if bool(b)==False:
    print(-1)