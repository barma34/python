#DAY-5
'''dictionary{}
dictionary is a mutable but duplicates are not allowed ( that means items with same key)
in dictionary are used to stored data in the formate of key=value
here the key are in the form of number,tuples or strings, this key are in case sensitive
syntax:
my_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}
'''

#barma={}
#print(type(barma))

# barma={1:'name',2:'father',3:'age',4:25,"hi":34}
# print(barma["hi"])

'''dictionary methods'''
#sathya={1:"kiran", 2:"python", "data":123, "age":24}
#print(sathya.get(2))
#print(sathya.keys())
#print(sathya.values())
#print(sathya.items())

# sathya.pop("age")
# print(sathya)

# sathya.update({"gopi":20}),sathya.update({"data":456})
# print(sathya)

# nested - dic within a dic
# dd={
#     'a':1,
#     'b':2,
#     'c':{3:'c',
#          4:'d',
#         }
#         }
# print(dd['c'][4])

#for i in {1: 'kiran', 2: 'python', 'data': 456, 'age': 24, 'gopi': 20}:
    #print(i)

# for k,v in {1: 'kiran', 2: 'python', 'data': 456, 'age': 24, 'gopi': 20}.items():
#     print(k,"==>",v)

'''tuple()
tuple are used to store multiple items in a single variable
tuple is a immutable
tuple is allowed duplicates
tuple has no methods
syntax'''
# sai=()
# print(type(sai))

# sai= (1, 2, 3, 'a', 'b', 'c')
# print(sai[1:5:2])

# sai=(1,3,5,6,8,2,23,57,42,343)
# print(len(sai))
# print(min(sai))
# print(max(sai))
# print(sum(sai))
'''tuple operations
concatenation
repetition
membership
iteration'''
# a=(1,2,3,4)
# b=(3,4,5,6)
# #print(a+b)
# l=[]
# for i,j in zip(a,b):
#     l.append(i+j)
# print(tuple(l))

# a=(1,2,3,4)
# print(a*4)

# a=(1,2,3,4)
# print(1 in a)
# print(7 not in a)

# a=(1,2,3,4)
# b=(5,6,23,67)
# print(a is b)
# print(a is not b)

# sum=0
# for naik in (2,34,12,67,54,90):
#     sum+=naik
# print(sum)