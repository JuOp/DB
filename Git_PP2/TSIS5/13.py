def copy_the_content(filename1, filename2):
    with open(filename1, 'r') as i:
        txt = i.read()
    with open(filename2, 'w') as i:
        i.write(txt) 

filename1 = input()
filename2 = input()
copy_the_content(filename1, filename2)