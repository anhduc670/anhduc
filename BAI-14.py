t = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
new = tuple(dict.fromkeys(t))
print(new)