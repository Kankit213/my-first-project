# string and conditional statement

print("hello world")
print("hello world","this is my first code")
a = 10
b = 2.6
c = "hello world"
print(type(a))
print(type(b))
print(type(c))

#data type and numeric and variables
a = 10
print(a) #variables
print(type(a))
b = 3.8
print(b)
print(type(b))
c = "hello print"
print(c)
print(type(c))
#boolean data type
a = True
print(a)
print(type(a))
b = False
print(b)
print(type(b))

#set data type
a = {"a","b","c"}
print(a)
print(type(a))

#sequence data type
#list
a = [1,2,3,4,5]
print(a)
print(type(a))

#tuple
a = (1,2,3,4,5)
print(a)
print(type(a))

#string

a = "python program"
print(a)
print(type(a))

#dictionary data type

a = {"key" : "value"}
print(a)
print(type(a))

#operators

a = 10
b = 20
sum = a+b
print(sum)

a = 30
b = 10
diff = a-b
print(diff)

a = 20
b = 5
multi = a*b
print(multi)

a = 50
b = 5
divide  = a/b
print(divide)

a = 30
b = 7
modules = a%b
print(modules)

a = 38
a += 1
print(a)

a = 45
a -= 2
print(a)

#assignment operator
#equal to operator
x = 25
print("x : ",x)

#add and equal to operator

a = 25
a+=5
print("a : ",a)

#substation and equal to

a = 300
a-=5
print("a : ",a)

#multi and equal to

a = 30
a*=5
print("a : ",a)

#decide and equal to

a = 500
a/=5
print("a = ",a)

#left shift assignment operator
a = 10
a<<=2
print("a : ",a)

#right shift assignment operator

a = 50
a>>= 3
print("a : ",a)

a = 50
b = 10
c = a&b
print("a : ",c)
print("b : ",b)

a = 20
b = 10
a^=b
print("a : ", a)

a = 50
b = 10
a /= b
print("a : ", a)

#comparison operator
#greater than
a = 30
b = 20
c = a>b
print(c)

#less than
x = 60
y = 50
xy = x<y
print(xy)

#greater than or equal to
a = 200
b = 40
x = a>=b
print(x)

#less than aur equal to

a = 40
b = 35
x = a>b
print(x)

#equal to

a = 40
b = 40
x = a==b
print(x)

#not equal to

a = 20
b = 30
x = a!=b
print(x)


#logical operator
#and operator

a = 20
print(a > 15 and a < 10)

#or operator
a = 15
print(a>12 or a<8)

#not operator
a = 15
print(a>10 and not a<12)

#identity operator
x = ["apple","mango"]
y = ["apple","mango"]
z = x
print(x is z) #that obj is matching that's why it returns true

print(x is y) #that obj is not matching that's why it has given false

#membership operator
x = ["apple","mango"]
print("banana" in x)

#not in operator
y = ["apple","mango"]
print("guava" not in y)



str1 = "This is the first string.\nWe are my own coding."
str2 = "This is the first string.  \t  we are my own coding."
print(str1)
str1 = "This is the first string.\nWe are my own coding."
print(str1)

str1 = "This is the first string.\nWe are my own coding."
print(str1)

name = "Apnea \n"
address = "collage"
mera = name + address
print(mera)

#indexing

str1 = "hello world"
len1 = len(str1)
print(len1)

a = "hello " + "" + "world"
print(a)
print(len(a))

str = "apnea collage"
ch = str[2]
print(ch)

str = "hello world"
bc = str[8]
print(bc)

#slicing
str = "helloworld"
print(str[0:11])
print(str[0 :])
print(str[0:5])
print(str[:5])

#slicing negative index

str = "hello world"
print(str[-8:-2])

#string function

str = "i am studying coding with apnea collage"
print(str.endswith ("age"))

str = "apnea collage"
print(str.endswith ("col"))

#capitalize
print(str.capitalize())
print(str)

#replace

print(str.replace("apnea" , "user"))

#find
str = "i am from studying from coding with apnea collage"
print(str.find("with"))

#count
print(str.count("from"))
print(str.count("a"))


#conditional conditions

#if statement

# age = 20
#
# if age>=18:
#     print("can vote me")
#     print("can driving licence")
#     print("bye")
#
# #elif statement
# #if_elif_else condition
#
# light = "yellow"
# if "light"== "yellow":
#     print("stop")
# elif "light"== "yellow":
#     print("go")
# elif light == "green":
#     print("look")
# else:
#     print("light is broken")
#
# print("end of code")
#
# age = 16
# if age>=18:
#     print("can vote")
# else:
#     print("cannot license")
#
#
# marks = int(input("enter marks : "))
#
# if marks >= 90 :
#     grade = "A"
# elif marks >= 80 and marks < 90:
#     grade = "B"
# elif marks >= 70 and marks < 80:
#     grade = "C"
# else:
#     grade = "D"
#
# print("grade of the student ->", grade)
#
#
# #nesting
# age = 90
#
# if age >= 18:
#     if age >= 80:
#         print("cannot drive")
#     else:
#         print("can driving")
# else:
#     print("cannot drive")
#
#
# #practice ques
#
# num = int(input("enter a number : "))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")
#
# num = int(input("enter : "))
# if num % 2 == 0:
#     print("even word")
# else:
#     print("odd word")
#
# #2
# a = int(input("enter the first number :"))
# b = int(input("enter the second number :"))
# c = int(input("enter the third number :"))
#
# if a >= b and a <= c:
#     print("a is greater : ",a)
# elif b>=c:
#     print("b is greater : ",b)
# else:
#     print("c is greater : ",c)
#
# #3
# x = int(input("enter the number : "))
#
# if x% 5 == 0:
#     print("multiple of 5")
# else:
#     print("not a multiple of 5")


#list

marks = [45.6,78.9,45.8,98.7]
print(marks)
print(type(marks))
print(marks[1])
print(marks[3])

#2
student = ["decline",123,56.7,"clever"]
print(student)
print(type(student))
print(student[0])
student[0] = "ankit"
print(student)
print(student[0])


#list slicing

marks = [45,67,87,89,54]
print(marks[1:4])
print(marks[:4])
print(marks[0:])
print(marks[1:5])
print(marks[-3:-1])

#list method

list = [2,3,4,5]
list.append(6)
print(list)

list = ["ankit","sonu","suraj"]
list.append("moti")
print(list)

#ascending order
list = [3,4,5,2,1]
print(list.sort())
print(list)

#descending order
list = [1,5,7,4,3,2]
print(list.sort(reverse = True))
print(list)

list = ['a','d','f','c','b','e']
print(list.sort(reverse = True))
print(list)

#reverse order

list = [2,3,4,5,6,7,8,9,2]
list.reverse()
print(list)

#insert

list = [3,4,2,1]
list.insert(2,5)
print(list)


#remove method
list = [2,3,1,4,5]
list.remove(3)
print(list)

#pop

list = [3,4,2,1,5]
list.pop(3)
print(list)

#tuples in python

tup = (2,3,4,5,6)
print(tup)
print(type(tup))
print(tup[0])
print(tup[1])

tup = (1,)
print(tup)
print(type(tup))

tup = (2,3,4,5,6)
print(tup[0:])
print(type(tup))

#tuple method

#index method
tup = (1,2,3,4,5,6,)
print(tup.index(6))

#count method
tup = (1,2,3,4,5,6,6)
print(tup.count(4))


#practice
#
# lis = ["Alibaba","here here","yantra"]
# print(lis)
# print(type(lis))
#
# movies = []
# mov1 = input("enter movie name : ")
# mov2 = input("enter movie name : ")
# mov3 = input("enter movie name : ")
#
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)
#
# list1 = [1,2,1]
#
# copy_list1 = list1.copy()
# copy_list1.reverse()
# if copy_list1==list1:
#     print("palindrome")
# else:
#     print("NOT palindrome")
#
# list2 = ["madam","ayah","madam","sir"]
#
# copy_list2 = list2.copy()
# copy_list2.reverse()
#
# if copy_list2 == list2 :
#     print("palindrome")
# else:
#     print(" NOT palindrome")
#
#
# list3 = [2,3,4,5,4,3,2,5]
# copy_list3 = list3.copy()
# copy_list3.reverse()
# if copy_list3 == list3:
#     print("palindrome")
# else:
#     print("NOT palindrome")

grade = ("a","c","d","a","a","c","a")
print(grade.count("a"))

list = ["a","c","d","a","a","c","a"]
print(list.sort())
print(list)

grade = ["C","D","A","A","C","A"]
grade.sort()
print(grade)

#dictionary in python

info = {
    "hello" : "world",
    "good" : "morning"
}
print(info)
print(type(info))

info = {
    "hello" : "world",
    "good" : "morning"
}
print(info)
print(type(info))

info = {
    "hello" : "world",
    "name" : "ankit",
    "learn" : "coding python",
    "learning" : ["python","java","c++","java script"],
    "topics" : ("dict","str"),
    "age" : 35,
    "is adult" : True,
    "marks" : 82.4
}
print(info)
print(type(info))
print(info["name"])
print(info["learn"])
print(info["learning"])
info["name"] = "ankit kumar"
print(info)
info["age"] = 18
print(info)
info["surname"] = "chaurashiya"
print(info)

nul_dict = {"ankit kumar"}
print(nul_dict)
nul_dict = {}
nul_dict["name"] = "ankit kumar"
print(nul_dict)

#nested dict

student = {
    "name": "subhash",
    "subject" : {
        "phy" : 89,
        "chem" : 95,
        "math" : 90

    }
}
print(student)
print(student["subject"])

print(student["subject"]["phy"])
print(student["subject"]["math"])

#key method dict

student = {
    "name": "subhash",
    "subject" : {
        "phy" : 89,
        "chem" : 95,
        "math" : 90

    }
}

print(student.keys())
print(student.values())

print(len(student.keys()))

#values method in dict

student = {
    "name": "subhash",
    "subject" : {
        "phy" : 89,
        "chem" : 95,
        "math" : 90

    }
}
print(student.values())
print(student)
print(student.values())

#.items method in dict

student = {
    "name": "subhash",
    "subject" : {
        "phy" : 89,
        "chem" : 95,
        "math" : 90

    }
}
print(student.items())
pairs = (student.items())
print(pairs)

#get method in dict

student = {
    "name": "subhash",
    "subject" : {
        "phy" : 89,
        "chem" : 95,
        "math" : 90

    }
}

print(student["name"])
print(student.get("name"))
print(student.get("subject"))

#update method in dict

student = {
    "name": "subhash",
    "subject" : {
        "phy" : 89,
        "chem" : 95,
        "math" : 90

    }
}
new_dict = {"city": "new town","age":18}
student.update(new_dict)
print(student)

#set in python

collection = {1,2,3,4,5}
print(collection)
print(type(collection))

collection = {"world",1,2,3,4,4,4,2,"hello","hello"} #set me not allowed in duplicate code
print(collection)
print(type(collection))

collection = {"world",1,2,3,4,4,4,2,"hello","hello"}
print(len(collection))

#null set in sets

collection = set() #empty sets : syntax
print(type(collection))

#add method in sets #add onw element

collection = set()
collection.add(1)
collection.add(2)
collection.add("hello")
print(collection)

#remove method in sets # remove an element
collection = {1,2,3,4,5,6}
collection.remove(2)
collection.remove(5)
print(collection)
print(len(collection))

#clear method in sets # clear data

collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
print(collection.clear())
print(len(collection))

#pop method in sets #removes a random values

collection = {"world","good morning","happy"}
(collection.pop())
(collection.pop())
print(collection)

#union method in sets #combines both set values and return new
set1 = {1,2,3,4,5,6}
set2 = {2,5,7,8,9}
print(set1.union(set2))

#intersection method in sets #combines common values and return new

set1 = {1,2,3,4,5,6}
set2 = {2,5,7,8,9}
print(set1.intersection(set2))


#practice
info = {
    "table" : ["a piece of furniture","list os lists and figures"],
    "cat" : "a small animal"

}
print(info)
print(type(info))
#2
set1 = {"python","java","c++","java script"}
set2 = {"java","python","java","c++","c"}

print(set1.union(set2))

subjects = {
    "python","java","c++","java script",
    "java","python","java","c++","c"
}
print(subjects)
print(len(subjects))

subject = {
    "python","java","c++"
}
print(subject)
subject = {"python","data analytics","c++"}
print(subject)

subject = {
    "name" : "ankit",
    "subject" : {
        "phy" : 89,
        "chem" : 95,
        "math" : 90
    }

}
print(subject)
print(subject.get("name"))

# marks = {}
#
# x = int(input(" enter phy :"))
# marks.update({"phy" : x})
#
# x = int(input(" enter math :"))
# marks.update({"math" : x})
#
# x = int(input(" enter chem :"))
# marks.update({"chem" : x})
# print(marks)

marks = {9 , "9.0"} #"" = string
print(marks)

# method 2
marks = {
    ("float",9),
    ("str",9.0)
}
print(marks)


#loops in python
#while loops.
count = 1
while count <= 5:
    print("hello")
    count += 1
print(count)

count = 1
while count <=10:
    print("hey mama")
    count += 1
print(count)

i=1
while i<=10:
    print("ankit",i)
    i=i+1

i = 5
while i>=1:
    print(i)
    i -= 1

i = 10
while i>=2:
    print(i)
    i=i-1
i = 1
while i<=100:
    print(i)
    i=i+1
i = 100
while i>=1:
    print(i)
    i=i-1
# i = 1
# while i<=10:
#     print(3*i)
#     i=i+1
# n = int(input("enter a number : "))
# i = 1
# while i<=10:
#     print(n*i) #than 14 table in loops
#     i=i+1
# print("ended")
#
# n = int(input("enter the number : "))
# i = 1
# while i<=10:
#     print(n*i)
#     i=i+1
# print("ended")

inx = 0
while inx< 10:
    print(inx)
    inx = inx+1

inx = 0
while inx <15:
    print(2*inx)
    inx = inx+1

#traverse

nums = [1,2,3,4,5,6,7,8,9,23,45,67]
inx = 0
while inx<len(nums):
    print(nums[inx])
    inx = inx+1
habits = ["hello","good","morning","hii","everything"]
inx = 0
while inx<len(habits):
    print(habits[inx])
    inx+=1

nums = [1,2,3,4,5,6,7,8,9,23,45,67]
x = 45
i = 0
while i<len(nums):
    if(nums[i]==x):
        print("hello world",i)
    else:
        print("finding---")
    i=i+1

nums = [23,45,67,43,21,56,54,32,67,78,54]
x = 54

i = 0
while i<len(nums):
    if(nums[i]==x):
        print("finally finding----",i)
    else:
        print("nahi mila")
    i =i+1


#break and continue
i = 0
while i<=5:
    print(i)
    if(i==4):
        break
    i=i+1

i = 0
while i<=10:
    print(i)
    if(i==7):
        break
    i = i+1
print("end of loops")

nums = [23,45,67,43,21,56,54,32,67,78,54]
x = 54

i = 0
while i<len(nums):
    if(nums[i]==x):
        print("finally finding----",i)
        break
    else:
        print("finding---")
    i =i+1
print("end of loops")

#continue

i = 0
while i<=5:
    if(i==4): #4 ko chokidar continue karo
        i = i+1
        continue
    print(i)
    i=i+1


x = 0
while x<=10:
    if(x==7): # 7 ko chokidar continue karo
        x = x+1
        continue
    print(x)
    x = x+1

x = 1
while x<=10:
    if(x%2==0): #odd number
        x = x+1
        continue
    print(x)
    x = x+1

x = 1
while x<=10:
    if(x%2!=0): #even number
        x = x+1
        continue
    print(x)
    x = x+1

#for loops

fruits = ["mango","apple","papaya","guava","orange"]
for value in fruits:
    print(value)
abc = [1,2,3,4,5]
for value in abc:
    print(value)
name = ["ankit","Susumu","Aditya","pooja"]
for value in name:
    print(value)

tup = (1,2,3,4,5,6)
for val in tup:
    print(val)

str = "ankitchaurashiya"
for char in str:
    print(char)

name = "ankitchaurashiya"
for char in name:
    if char == "i":
        print("i found")
        break
    print(char)
print("end")

abc = (1,2,3,4,5)
for value in abc:
    if value == 4:
        print("4 found")
        break
    print(value)
print("end")

abcd = [4,8,9,16,25,32,49,64,81,100]
for val in abcd:
    print(val)


#leaner search
abcd = [4,8,9,16,25,32,49,64,81,100,25,32]
x = 32
inx = 0
for el in abcd:
    if el== x:
        print("found",inx)
    inx+=1

numbers = [12+34+56+67+67]
total =0
for num in numbers:
    total=total+num
print("total",total)

numbers = [1200*345+800]
total = 0
for num in numbers :
    total = total + num
print("total",total)

#range function in loops

for i in range(14,20):
    print(i)
print(range(6))

for i in range(2,16,2):  #even number print
    print(i)

for i in range(1,50,2): #odd numbers print
    print(i)

#practice

for i in range(1,101): #ascending order
    print(i)

for i in range(101,50 ,-1) : #descending order
    print(i)

# User se number lo
# n = int(input("enter a number: "))
# for i in range(1,11):
#     print(n*i)

#pass statement in loops

for i in range(10):
    pass
print("end the obj ")
for i in range(5):
    pass
print("end ")

n = 5
sum  = 0
for i in range(1,n+1):  #1 se lexer 5 tak add
    sum  += i
print("total sum =", sum)

n = 100
sum = 0
for i in range(1 ,n+1): #1 se lexer 100 tak add
    sum +=i
print("total sum =", sum)

n = 25
sum = 0
for  i in range(1,n+1):
    sum += i
print("total sum =", sum)

n = 20
sum = 0
i = 1
while i<=n:
    sum += i
    i += 1
print("total sum =", sum)

n = 10
sum = 0
i = 1
while i<= n:
    sum += i
    i += 1
print("total sum =", sum)

n = 18
sum = 0
i = 1
while i<=n:
    sum +=i
    i += 1
print("total sum =", sum)

n = 5
fact = 1
i = 1
while i<=n:
    fact *= i # 1 se lekar 5 tak multiply
    i += 1
print("total fact =", fact)

n = 12
fact = 1
for i in range(1,n+1):
    fact *= i
print("total fact =", fact)

n = 5
fact = 1
for i in range(1,n+1):
    fact *= i #factorial = multiply to 5 to 1
print("total fact =", fact)


#Function  definition in python 

def add(a,b): #parameters
    return  a+b
sum = add(10,20)  #  function call : arguments
print("sum =",sum)  

def sub(a,b):
    return a-b
diff = sub(20,10)
print("diff =",diff)

diffn = sub(100,20)
print("diffn =",diffn)


def hello_world():
    print("hello world")
print(hello_world())    
print(hello_world()) 
print(hello_world()) 
print(hello_world()) 
print(hello_world()) 

def print_name(name):
    print("hello", name)
    
print_name("Ankitchaurashiya")



def print_name(name):
    print("hello : ", name)
print_name("Annupriya")    

def print_hello():
    print("hello")
print_hello()    
print_hello()

def avg_marks(a,b,c):
    return (a+b+c)/3

avg = avg_marks(90, 90, 78)
print("Average marks:", avg)


def avg_marks(a,b,c):
    return(a+b+c)/3
avg = avg_marks(90, 90, 95)
print("Average marks:",avg)


print("hello world" , end ="") # end = "" : print in same line
print(" hello world my journey") #

def cal_product(a,b=2):
    print(a*b) #default parameter
    return a*b
cal_product(9)

#practise

cities = ["delhi " ,"rajsthan", "mumbai", "gova " , " chennai"] # list me len nikalna  
heroes = ["thor","heroman","tejm","thor","saktiman ","heroman","tejmaro","thor",]
print(heroes[2], end = " ")
print(heroes[3], end = " ")

def print_length(list):
    return len(list)
print(print_length(heroes))
print(print_length(cities))

cities = ["delhi " ,"rajsthan", "mumbai", "gova " , " chennai"]

def print_list(list):
    for city in list:
        print(city, end = " ")
print()        
print_list(cities)       


heroes = ["thor","heroman","tejm","thor","saktiman ","heroman","tejmaro","thor",]
def print_length(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item)
print_list(heroes)
print()      


def print_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print("total fact =", fact)
print_factorial(7) # 1*2*3*4*5*6*7 = 5040 karna 

x = 5
factorial = 1
for i in range(1,x+1):
    factorial *= i
print("total fact =", factorial)


def converter(us_values): # us doller se inr me convert karna
    inr_values = us_values * 82.74
    print(us_values,"usd = ",inr_values,"INR ")

converter(100)


def converter(usd_values):
    inr_values = usd_values*83.00
    print(usd_values,"USD =",inr_values,"INR")
converter(1)   

#recuron loops hi hai in python 

def show(n)  :
    if (n==-1) :
        return
    print(n)
    show(n-1)
show(6)

def show(n):
    if(n  == 0):
        return
    print(n)
    show(n-1)
show(10)    

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("end")
show(4)    

#recorson factorial

def fact(n):
    if(n==1 or n==0):
        return 1
    return fact (n-1)*n
print(fact(4))


#practise 
def fact(n):
    if(n == 1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(5))


def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1)+n
sum = (cal_sum(50))    
print(sum)


def print_list(list,inx=0):
    if(inx==len(list)):
        return
    print(list[inx])
    print_list(list,inx+1)

fruits = ["apple","banana","papaya","orange","mango"]
print_list(fruits)


def print_list(list,inx=0):
    if(inx==len(list)):
        return
    print(list[inx])
    print_list(list,inx+1)

heroes = ["benten","motupatlu","balbeer","rani-pari","thorman"]
print_list(heroes)

#oop in python 

class Student:
    name = "ankit"
    colour = "chikhna"
s1 = Student()
print(s1.name)
print(s1.colour)

#__init__ function 

class Student:
    #name = "priya"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new daa in database.")

s1 = Student("priya",96)
print(s1.name, s1.marks)
s2 = Student("rohit",78)
print(s2.name, s2.marks)

        
#class & instance attributes

class Student:
    collage_name = "any university"
    name = "pooja"

    def __init__(self,name,msrks):
        self.name = name
        self.marks = marks
        print("adding new data ")

s1 = Student("karan",88)
print(s1.name)

#methods

class Student:
    collage_name = "abc collage"

    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks

    def welcome(self):
        print("welcome student",self.name)

    def get_marks (self):
        return self.marks

s1 = Student("karan", 88)
s1.welcome()
print(s1.get_marks())

#lets practise 

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum +=val
        print("hii",self.name,"your avg score",sum/3) 
s1 = Student("aryan vindra",[89,98,98]) 
s1.get_avg()

s1.name = "viivek vindra"
s1.get_avg()


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hiii", self.name,"your avg score:"  ,sum/3)


s1 = Student("aryan malhotra",[78,90,87])
s1.get_avg()
        
#static methodd

class Student:
    @staticmethod
    def collage():
        print("apna collage")
        
s1 = Student()
s1.collage()

#IMPORYTANT

##abstraction
class Car:
    def __init__(self):
        self.clutch = False
        self.acc = False
        self.brake = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

car1 = Car()
car1.start()


#practise 

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount, "was debited")
        print("total balance = " , self.get_balance())

    def credited(self,amount):
        self.balance += amount
        print("Rs",amount,"was created")
        print("total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(100000,12000)
acc1.debit(12000)
acc1.credited(12000)

#del in python 

class Student:
    def __init__(self,name):
        self.name = name
s1 = Student("ankit")
print(s1.name)
del(s1.name)
print(s1)

#private attributes & methods

class Account:
    def __init__(self , acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    def reset_pass(self):
        print(self.__acc_pass)
s1 = Account("12345","abcdef")
print(s1.acc_no)
print(s1.reset_pass())

#2 
class Person:
    __name = "anonymus"

    def __hello(self):
        print("hello person")
    def welcome(self):
        self.__hello()



p1 = Person()
print(p1.welcome())

#inheritance
#single line heritance

class Car :
    colour = "black"
    @staticmethod
    def start():
        print("car started.")
    @staticmethod
    def stop():
        print("car stopped")

class Toyatacar(Car):
    def __init__(self,name):
        self.name = name
car1 =  Toyatacar("fortuuner")
car2 = Toyatacar("mercidies")
print(car1.colour)

#multi level heritance
 
class Car:
    @staticmethod
    def start():
        print("car started... ")
    @staticmethod
    def stop():
        print("car stopped...")
class Toyatacar(Car):
    def __init__(self,brand):
        self.brand = brand
class Fortuner(Toyatacar):
    def __init__(self,type):
        self.type = type
car1 = Fortuner("dieseal")
car1.start()

#multiple level 

class A:
    varA = "welcome to class A"   
class B:
    varB = "welcome to class B"    
class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

#super method 

class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop ():
        print("car stopped")
class Toyatacar(Car):
    def __init__(self,name,type):       
        
        super().__init__(type)
        self.name = name
        super().start()

      

car1 = Toyatacar("priyus","electrician")
print(car1.type)

# class method 
class Person:
    name = "anonymous"
    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("rohit kumar")
print(p1.name)
print(Person.name)




