################################################################################################
'''DAY-1'''
"""this a basic code and welcome note"""
#print("hello python") 
########################
 # comments is a messsage of someting to defind
''' there are two types of comments
1. single-line or (in line) rep (#)
2. multi-line or (block) rep (''' ''' or """  """)'''

'''variable'''
'''is a container which store a value'''
'''rules
a variable name is start with latter or underscore( _ ) symbols are not allowed any case
ex:name(name=123) or _name(_name=456)
variable names are case-sensitive for print output
the reserved keywords con't be use as a variable name , classes name and functions name
in python 35 keywords depending on python update
ex: ...google it'''
   
'''syntax :
    let age = 24 
    here 'age 'rep container or variable and  '24'rep value'''

'''single variable to single value'''
#naik=1995
'''single variable to multiple value'''
#naik=100,200,300
'''multiple variable to multiple values'''
#a,b,c=10,20,30
'''multiple variable to single value'''
#a=b=c=d=100
'''find address of variable for use this # print(id(variable name))'''

'''variable cases
1.camelCase  .....ex:paythonLife
2.snake_case .....ex:paython_life
3.PascalCase .....ex:PaythonLife'''
##############
'''data_type
a data type in programming is classification that specifies which type of value a variable
ref: google it
1.numeric
    1.integer ... intclass(20 ,-20) 
    2.float ..... floatclass(2.3333)
    3.complex..... real+imag(2+3j)
    syn '''

# a= 10 
# b=-10 
# c=3.33 
# d=-4.25 
# e=True 
# f=False 
# g=2+4j 
# h=4+5j
# print (type(a),type(b),type(c),type(d),type(e),type(f),type(g),type(h))

'''type conversions
converting one type to another type 
1.implicit .....when a compiler automatically converts data types without data loss.
2.explicit .....the process of manually changing a value's data type from one to another within a program data loss.
'''

# #simple intrest
# p=1000
# t=2
# r=20
# print((p*t*r)/100)

# #compond intrest
# p =1000
# r=20
# n=1
# t=3
# print(p*(1+r/n)**n*t)

#area of triangle
# base=20
# height=30
# print(1/2*(base*height))
###############################################################################################


'''DAY-2'''
'''operator
is a symbols is used for the operations on values and variables
there are 7 types ref: pdf
1.arithmetic operators (/,//,*,+,-,=)'''

# a=7
# b=2
# print('sum:',   a+b)
# print('sub:',   a-b)
# print('mul:',   a*b)
# print('div:',   a/b)
# print('fdiv:', a//b)
# print('mul:',   a%b)
# print('pow:',  a**b)
'''assignment operater'''
# a=10
# b=5
# #a += b
# a -= b
# print (a)

# a=5
# b=2
# print ('a==b=', a==b)
# print ('a!=b=', a!=b)
# print ('a>b=', a>b)
# print ('a<b=', a<b)
# print ('a>=b=', a>=b)
# print ('a<=b=', a<=b)
'''logical operators(and ,or, not)'''
#and * or+ not
'''control statements 
1.conditional(if,if-else,if-elif-else,nested_if-else(if inside if ))
2.transfer or jumping (break,continue,pass)
3.iterative or lopping(for,while)'''

# age=int(input('enter age'))

# if age>18 :
#     print('nenu if')
# elif age<18:
#     print('nenu elif')
# else:
#     print('nenu else')

# branch_names = ['EEE', 'CIVIL', 'MECH', 'ECE']

# name_to_find = input('stingray=')

# if name_to_find in branch_names:
#     print("yes your b-tech")
# else:
#     print("no your not b-tech")


# if True:
#     print('this is outer if')
#     if False:
#         print('this is inner if')
#     else:
#       print('this is inner else')
# else:
#    print('this is outer else')
''''nested-if'''
# number = int(input("Enter a number: "))

# if number > 0:
#     print("The number is positive.")
#     if number % 2 == 0:
#         print("The number is also even.")
#     else:
#         print("The number is also odd.")
# elif number < 0:
#     print("The number is negative.")
#     if number % 2 == 0:
#         print("The number is also even.")
#     else:
#         print("The number is also odd.")
# else:
#     print("The number is zero.")


'''short hand if
short hand if else
a=1
b=2
#if a<b:print(a)
print(a) if a>b else print(b)'''

# username='naik'
# passw=1234
# user =input("enter user name:")
# passw =input("enter user password:")
# if user==username and passw==passw:
#     print('welcome')
# else:
#     print('login again')

'''2-looping
it execute a group of statements multiple time you use looping statements(while,for,nested lopps)
for'''
# for naik in range(1,20,2):
#     print(naik)

# for naik in "pythonlife":
#     print(naik)

# for naik in ("barma"):
#     print(naik)
#a=True
# while a<5:
#     print('naik')
#     break

# for language in ('python'):
#     for char in (language):
#         print(char,end=' ')
#     print( )

# for i in range(0, 5):
#     for j in range(i):
#         print(i, end=' ')
#     print()

# naik=1
# while naik<5:
#     print('barma', naik)
#     naik+=1

# i=1
# while i<3:
#     print(i,"barma")
#     j=1
#     while j<3:
#         print(j,"naik")
#         j+=1
#     i+=1

# if True:
#     pass

##############################################################################################
'''DAY-3'''
'''LIST-[]
list is used to stored various type of data like (10,'naik',4.25, bool,(3,5,7))
1.mutable-modify data
refer: class notes
'''
# naik=[1,2,3,4,'B','A','R','M','A']
#print([4]) positive index
# print(naik[-2]) negative index
# naik[0]='naik' modify index
# print (naik)
'''slicing'''
#naik=[1,2,3,4,'B','A','R','M','A']
#print(naik[4:9])positive
#print(naik[2:9:2]) skip positive
#print (naik[-8:])negative back move
#print (naik[:-3]) negative forwd move
#print(naik[::])
#print(naik[::-1])
'''list methods'''
# 1.append
# naik=[1,2,3,4,'B','A','R','M','A']
# naik.append(["barma",5,6])
# print(naik)

# 2.extend
# naik=[1,2,3,4,'B','A','R','M','A']
# #naik.extend(["naik", 5,6,])
# naik.extend(["naik"])
# print(naik)

# 3.copy
# naik=[1,2,3,4,'B','A','R','M','A']
# barma = naik.copy()
# naik.append("xyz")
# print(naik)
# print(barma)

# 4.clear
# naik=[1,2,3,4,'B','A','R','M','A']
# naik.clear()
# print(naik)

# 5.count
# naik=[1,2,3,4,'B','A','R','M','A',1,4]
# print(naik.count("A"))

# # 6.index
# naik=[1,23,3,23,4,23]
# print(naik.index(3))
#print(len(naik))
# for i in range(len(naik)):
#  if naik[i]==23:
#      print(i)
# print(naik)

# 7.insert
# naik=[1,2,3,4,'B','A','R','M','A']
# naik.insert(5,".naik")
# print(naik)

# 8.pop
# naik=[1,2,3,4,'B','A','R','M','A',2]
# naik.pop(1)
# print(naik)

# 9.remove
# naik=[1,2,3,4,'B','A','R','M','A',2]
# naik.remove(2)
# print(naik)

# 10.reverse
# naik=[1,2,3,4,'B','A','R','M','A']
# naik.reverse()
# print(naik)

#11.sort
#naik=[4,1,3,2,8,4,6,9,15,3]
#naik.sort()
# naik.sort(reverse=True)
# print(naik)


