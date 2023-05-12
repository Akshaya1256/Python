set1={'a','b','c','d','e'}
print(set1)
set1.add('f')
print(set1)
set2={'g','h','i','j'}
set1.update(set2)
print(set1)
set1.discard('h')
print(set1)
for i in set1:
    print(i)
print(list(set1))
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
