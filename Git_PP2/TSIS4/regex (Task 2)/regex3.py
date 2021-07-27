import re
x = input()
y = re.findall('[0-9]*[a-zA-Z]*', x)
for i in y:
    z = False
    for j in range(1, len(i)):
        a=i[j-1]
        b=i[j]
        if a==b:
            print(a)
            z = True
            exit()
    if z: exit()
if z == False:
    print(-1)