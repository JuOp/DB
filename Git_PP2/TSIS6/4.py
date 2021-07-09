a = input()
def reser(string):
    string2 = ''
    index = len(string)
    while index > 0:
        string2 += string[index-1]
        index = index - 1
    return string2
print(reser(a))