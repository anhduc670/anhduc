t = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
new = tuple(x for x in t if t.count(x) == 1)
print(new)