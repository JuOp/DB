def longest_word(filename):
    txt = open(filename)
    text = txt.readlines()
    lng = ''
    for i in text:
        a = i.split()
        for j in a:
            if len(lng) < len(j):
                lng = j
    print(lng)

longest_word('input.txt')