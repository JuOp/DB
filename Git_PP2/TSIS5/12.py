def write_list_into_file(filename, LiSt):
    with open(filename, "w") as myfile:
        for i in LiSt:
                myfile.write("%s\n" % i)

LiSt = input()
filename = input()
content = open(filename)
print(content.read())