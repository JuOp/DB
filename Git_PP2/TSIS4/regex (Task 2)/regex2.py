regex_pattern = r""	# Do not delete 'r'.
import re
s = input()
a = re.split('[.,]', s)
for i in a:
    print(i)