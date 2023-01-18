def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)
    
print(highest_even([1,2,3,4,22,5,6,7,8,9,10,11]))