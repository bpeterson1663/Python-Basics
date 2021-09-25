import re

pattern = re.compile('this')
string = 'search for this inside of this text please!'

a = pattern.search(string)

print(a.span())
print(a.group())
