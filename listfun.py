persons=[['akshaya','sowmya','kavitha'],[17,20,42],['stu','stud','hf']]
print(persons[0])
print(persons[0][2])
persons.append('reddy')
persons.pop(1)
print(persons)
print(persons[:2])
persons.reverse()
print(persons)
persons[2].insert(1,'nandu')
print(persons)
per=[1,5,2,4]
persons.extend(per)
print(persons)
persons[1].remove('hf')
print(persons)
print(persons[1].count('stu'))

