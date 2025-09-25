# def greet():
#     print("hello world")
# greet()

# def my_function(name):
#     print("hello",name)
# my_function("world")

# def add(a,b):
#     print("sum is: ",a+b)
# add(5,10)

# def introduce(name,age):
#     print(f"my name is {name},my age is {age}")
# introduce(name ="sathvika",age = 17)

# def my_function(name ="guest"):
#     print("hello",name)
# my_function()
# my_function("ram")

# x = 100
# def func():
#     y = 50
#     print("inside function,x=",x)
#     print("inside function,y=",y)
# func()
# print("outside function,x=",x)
# print(y)

# a =int(input("enter a value: "))
# b= int(input("enter a value: "))
# def function(a,b):
#     print(a*b)
# function(9,4)

# num = int(input("enter a num: "))
# def function(num):
#     if num%2==0:
#       print("even")
#     else:
#        print("odd")
# function(num)

# a =int(input("enter a value: "))
# b= int(input("enter a value: "))
# c= int(input("enter a value: "))

# def function(a,b,c):
#   if (a>b>c or a>c>b):
#       print("a")
#   if(b>a>c  or b>c>a):
#       print("b")
#   if(c>b>a or c>a>b):
#       print("c")
# function(a,b,c)

# name = (input("enter name: "))
# def function(name):
#     print(name[::-1])
    
# function(name)


# a = int(input("enter number: "))
# def func(n):
#     result = 1
#     for i in range(1,n+1):
#         result*= i
#     print(result)
# func(a)

# name = (input("enter name: "))
# def func(name):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in name:
#         if char in vowels: 
#          count+=1
#     print(count)
# func(name)

# def square(x):
#     return x*x
# number = [1,2,3,4,5]
# squared = list(map(square,number))
# print(squared)

# def is_even(x):
#     return x%2==0
# number = [1,2,3,4,5,6]
# even_numbers = list(filter(is_even,number))
# print(even_numbers)

# from functools import reduce
# def add(x,y):
#     return x+y
# numbers = [1,2,3,4,5]
# sum_numbers = reduce(add,numbers)
# print(sum_numbers)