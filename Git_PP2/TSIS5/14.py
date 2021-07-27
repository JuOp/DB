def combine(filename1, filename2):
    with open(filename1) as txt1, open(filename2) as txt2:
        for x, y in zip(txt1, txt2):
            print(x+y)

filename1 = input()
filename2 = input()
combine(filename1, filename2)