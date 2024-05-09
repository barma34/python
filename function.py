# type: ignore
'''function > is a  Block of code which only run when it is called.
# '''
# def fun_name(): # function defination
#     # function body
#     print('this is a function')

# fun_name() #function call
# fun_name()

# for i in range(3):
#     fun_name() # function call

# def vikas(a,b): # here "a,b" is called parameter or arguments
#     print("hi",a,b)
# vikas(10,20)

# def chari(*a): # a* arbitary argument take a data like a tuple
#     print(a)
# chari(100,10,20,30)
# chari([100,10,20,30]) # for this condition no needs *a=a

# def chari(**a): # this type is kwargs argument take a data dic
#     print(a)
# chari(a=2,b=3)

# def sum (a,b):
#     print(a+b)
# def sub (a,b):
#     print(a-b)
# def mul (a,b):
#     print(a*b)
# def div (a,b):
#     print(a//b)

# sum (12,4)
# sub (12,4)
# div (12,4)
# mul (12,4)
#import -> from file name import *

'''advance_function
lambda_function > this function is a small anonymous function
a lambda function can take any number of arguments, but canonly have one expression
syntax:
f=lambda a:a*a

f=(function object that accepts and stores the result of the expression)
lambda=keyword
a= argument
a*a= one line expression
'''
# x=lambda a,b,c:a*b+c
# print (x(5,2,1))

# x=[12,34,5,6,8]
# y=[]
# for i in x:
#     z=lambda a:a+1
#     y.append(z(i))
# print(y)

'''filter
syntax
filter(function, sequence)
parameters
function: function that tests if each element of a sequence true or not
sequence: sequence which needs to be filtered ,it can be a set ,lists, tuples or containers
of any iterators.
returns: returns an iterator that is already filtered'''

# age = [5,18,25,14,16,20,27]

# def myfun(x):
#     if x >= 18:
#         return True
#     else:
#         return False
    
# adults = filter(myfun, age)
# print(list(adults))

'''te python map() function is used to return a list of results after applying a given
function to each item of an iterable(list,tuple etc..)
syntax
'''
# def caladd(n):
#     return n+n
# number =(1,2,3,4)
# result = map (caladd ,number)
# print(list(result))

'''
the reduce() is a applies a given function to the iterables and returns a single value
'''
# from functools import reduce
# # reduce (function,sequence)
# d=reduce(lambda a,b: a+b,[23,54,32,54,98])
# print(d)

'''generater
this function defined like a normal function ,but whenever it needs to generate a value
it does so with the yield keyword rather than return
if the body of a def contains yield,the function automatically becomes a generater function
'''
# def sim_gen():
#     yield 1 # pause or hold
#     yield 2
#     yield 3
# x =sim_gen()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

'''yield 
this statement is responsible for controlling the flow of the generater function
it pause the function execution by saving all states and yielded to the caller
later it resumes execution when a successive function is called we can use
the multiple yield statements in the generater function

the return statement returns a value and terminates the whole function and only one return
statement can be used in the function'''
