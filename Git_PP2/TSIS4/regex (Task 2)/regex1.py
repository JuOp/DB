import re
y=int(input())
ans=[]
for i in range(0, y):
    txt = input()
    x = re.match('[-+]?[0-9]*\.[0-9]+$', txt)
    ans.append(bool(x))
for i in ans:
    print(i)
