'''set{}
set is collection which is unordered and unindexed,this set are not allow duplicate values
it can have any number of items and they may be of diffrent types{int,float,tuple,string,
etc..}but a set conot have mutable elements like lists setsor dictionaras its elements '''

sruthi={1,2,5,5,4,3,5,4,}
#print(type(sruthi))
#print(sruthi)


# letter = 'jsdjjlkhajkjafislAJAJLJLDUWP'

# string_letter=str(letter)
# list_letter=list(letter)
# tuples_letter=tuple(letter)
# set_letter=set(letter)

# print(string_letter)
# print(list_letter)
# print(tuples_letter)
# print(set_letter)

'''set methods
add..,clear..,copy..,pop..,remove..,update..'''
hema={15,2,4,56,51,84,94,364}
# hema.add('naik'),hema.add(43)
# print(hema)

# hema.remove(51)
# print(hema)

# hema.pop() # it remove small element
# print(hema)

# hema.update({'abc',1})
# print(hema)

'''set operations
union..,difference..,intersection..,isdisjoint..,issubset..,issuperset..,
symmetric_difference  '''

# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
#print((set1).union(set2))
#print(set1.intersection(set2))
#print(set1.symmetric_difference(set2))
#print(set1.difference(set2))
#print(set1.isdisjoint(set2))

# set1={1,2,3,4}
# set2={1,2,3,4,5,6,7,8,5,25,76,}
# print(set1.issubset(set2))
# print(set1.issuperset(set2))

'''frozenset
this function returns an immutable frozen object initialized with elements from 
given iterable'''
sunny=[1,2,5,7,9,12,54,31]
print(type(sunny))
b=frozenset(sunny)
print(type(b))