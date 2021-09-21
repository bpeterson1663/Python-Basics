import datetime
from array import array
from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 7, 7]
print(Counter(li))
sentence = 'blah blah blah'
print(Counter(sentence))

dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(dictionary['c'])  # returns 5 since c doesnt exist

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d)  # False because the order does not match

print(datetime.time(5, 45, 20))

arr = array('i', [1, 2, 3])

print(arr[0])  # 1
