import re
txt = input()
x = re.findall('\d+', txt)
for i in x:
    print(i)