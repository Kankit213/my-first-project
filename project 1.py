# to YouTube practice set

#type conversion
a = 5
b = 5.4
sum = a + b
print(sum)

a = "10"
b = int(a)
print(b+5)

a = 55.8
b = float(a)
print(b+5)

print(float(3+5))

value = 9.99
print(int(value))

#boolean and list me casting

print(bool(0))
print(bool(5))
print(bool(""))
print(bool("5"))

print(list("abc"))
print(list((1,2,3,4)))
print(list(range(15)))

#tuples
numbers = [1.2,3,4,5,6,6,5,7,4,3,2]
print(tuple(numbers))
print(set(numbers)) #duplicate hat gaye

print(round(9.99))

#input in python

# val = float(input("entered some value : "))
# print("you entered :",val)
# print(type(val),val)
#
# value = float(input("entered some value : "))
# print("you entered : ",value)
# print(type(value),value)

# name = input("what is your name? : ")
#
# age = input("what is your age? : ")
# marks = input("what is your marks? : ")
# print("name",name)
# print("age",age)
# print("marks","name","age"),

# a = first = int(input("entered first number: "))
# b = second = int(input("entered second number: "))
# c = third = int(input("entered third number: "))
# print("sum =",a + b + c)

# side = float(input("enter square side : "))
# print("ares : ",side**2)
#
# a = float(input("enter first number: "))
# b = float(input("enter second number: "))
#
# print("average : ",(a+b)/20)
#

#string

#indexing
fruit = ["apple", "banana", "cherry"]
print(fruit[(2)])
print(len(fruit))

#slicing

fruits = "apnea collage"
print(fruits[2:9])
name = "ankit kumar chaurashiya"
print(name[0:])

#slicing negative marks

fruits = "apple mango"
print(fruits[-7:-1])

#str function

fruits = "apple banana mango"
print(fruits.endswith("mango"))
print(fruits.capitalize())
print(fruits.replace("mango","guava"))
print(fruits.find("le"))
print(fruits.count("mango"))


#conditional statement

marks = 75

if marks>=85 :
    print("a grade")
elif marks>=75:
    print("b grade")
else:
    print("fail")

marks = 79

if marks>=90:
    (print("a+ grade"))
elif marks>=80:
    (print("b+ grade"))
elif marks>=70:
    (print("a+ grade"))
else:
    print("fail")

# day = "friday"
# if day=="saturday" or day=="friday":
#     print("holiday")
#
# username = input("Username: ").strip()
# password = input("Password: ").strip()
#
# if username == "ankit" and password == "1234":
#     print("Welcome, Ankit!")
# elif username == "ankit":            # username सही, password गलत
#     print("Password गलत है।")
# else:
#     print("User नहीं मिला।")
#
# fruits = input("fruits : ").strip()
# vegetables = input("vegetables : ").strip()
#
# if fruits == "banana" or vegetables == "potato":
#     print("healthy and fresh")
# elif fruits == "apple" or vegetables == "cherry":
#     print("good and fresh")
# else:
#     print("mite hai")
#
# signal = input("signal : ").strip()
#
# if signal== "red":
#     print("you are dangerous")
# elif signal == "green":
#     print("you are good")
# else:
#     print("you are bad")


#list in python

marks = [7,8,9,5,4,3]
print(marks[5])
print(len(marks))

#list slicing
marks = [7,8,9,5,4,3,8,6,5,4]

print(marks[0:])
print(marks[:])
print(marks[5])
print(marks[-5:-1])


#list method
list = [1,2,3,5,]
list.append(3)
print(list)

list.sort()
print(list) #ascending order
list.sort(reverse=True) #descending order
print(list)

list.reverse()
print(list)

list.insert(5,9)
print(list)

list = [1,2,5,4,5,6,5]
list.remove(6)
print(list)

fruits = ["apple", "banana", "cherry", "mango"]
last = fruits.pop()
print(last)
print(fruits)
print(last)

#tuples in python

a = (1,2,3,4,5,56,67,8)
print(a[6])
print(type(a))

tup = (3,4,5,6,7,5,5,5)
print(tup.index(5))

print(tup.count(5))

#dictionary in python

dict = {
    "name" : "ankit",
    "age" : "18"

}

print(dict["name"])
print(dict)
print(dict["age"])

#nested dictionary

info = {
    "name" : "ankit",
    "age" : "18",
    "marks" : 97,
    "village" : "Marena",
    "score" : {
        "math" : 89,
        "physics" : 80,
        "chemistry" : 70,

    }

}
print(info["name"])
print(info["score"])
print(info["village"])

info["village"] = "nowadays"
print(info["village"])

info["marks"]  =  "82.2"
print(info["marks"])
print(info["score"]["physics"])
info["professional"] = "cricket"
print(info["professional"])
print(info)
info["nation"]  = "indian"
print(info)

#dict method

info = {
    "name" : "ankit",
    "age" : "18",
    "marks" : 97,
    "village" : "Marena",
    "score" : {
        "math" : 89,
        "physics" : 80,
        "chemistry" : 70,

    }

}

print(info.keys())
print(info.values())
print(info.items())
print(info.get("score"))

info.update({"girls" : "not allowed"})
print(info)

info.update({"nation" : "indian"})
print(info)

#set in python

nums = {1,2,3,4,5,6,7,8}
print(nums)
print(type(nums))

#set method

set = set()
print(set)

nums = {1,2,3,4,5,6,7,8,9}

print(nums.add(11))
print(nums)
print(nums.add(12))
print(nums)
print(nums.remove(12))
print(nums)
print(nums.remove(1))
print(nums)

print(nums.clear())
print(nums)
marks = {34,56,78,90,65,32,56.54,45}
marks2 = {67,89,54,32,14,78,90}
print(marks.pop())
print(marks)
print(marks2.pop())
print(marks2)


marks = {34,56,78,90,65,32,56,54,45}
marks2 = {67,89,54,32,14,78,90}
print(marks.union(marks2))
print(marks.intersection(marks2))




