from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7,7,7]
sentence = 'blah blah blah thinking'
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(dictionary['c']) 

od = OrderedDict()
od['a'] = 1
od['b'] = 2

od2 = OrderedDict()
od2['b'] = 2
od2['a'] = 1

print(od == od2) # returns false since order is not the same