import re

#ff = open('data.txt', 'r')
#data = ff.read()
#ff.close()

with open("C:\Users\User\Desktop\Git_PP2\TSIS4\data.txt") as fa:
   text = fa.read()
   
name = re.search(r'Филиал\sTOO\s\w+\s\w+', data)
bin = re.search(r'\d{12}', data)
items = re.findall(r'\d+\.\n(.*)', data)
cnt = re.findall(r'(\d),\d{3}', data) # <- pattern
price = re.findall(r'x\s([\d\s]+,\d+)', data)
total = re.findall(r'Стоимость\n([\d\s]+,\d+)', data)
address = re.search(r'г\.\s[\w\-]+\,\w+\,\s[\w+\s]+\,\d+\,\s\w+\-\d', data)
date = re.search(r'\d{2}\.\d{2}\.\d{4}\s\d{2}\:\d{2}\:\d{2}', data)

#print(name)
print("1. Name of company: " + name.group())
print("2. BIN number: " + bin.group())

for i in range(len(items)):
    #print(len(items))
    print("1. Title: " + items[i])
    print("2. Count: " + cnt[i])
    print("3. Unit price: " + price[i])
    print("4. Total price: " + total[i])

print("5. Date: " + date.group())
print("6. Address: " + address.group())