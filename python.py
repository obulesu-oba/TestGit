#!/usr/bin/env python
# coding: utf-8

# In[3]:


#a = 20
# = 30
a = input('variable of the result is :')


# In[2]:


A = '35'
b = 50
c = int(A)+b
print(c)


# In[3]:


print("Welcome")


# In[4]:


a=12
b=15
print(a*b)


# In[5]:


2*5


# In[6]:


3+4


# In[7]:


a = 5
b = 10
c = a+b
c


# In[8]:


#variable
a = 10
b = 10.5
c = "welcome"
print(a)
print(c)


# In[4]:


a=b=c=50
print(a+b)
print(a-b)
print(a*b)
print(b)
print(a+b-c)


# In[10]:


a,b,c = 50,52,56
print(a)


# In[11]:


a,b,c=20,10,15
print(a+b+c)


# In[12]:


#Different ways to excute programms
#1.command promt
#2.text editer
#3.IDE(IDEL)


# In[13]:


#first to use text editer before you were do one thing 
#Take a any one of the text editer and put into data and save any where in local system 
#After that open command promt and change directory where as your fille was saved and select them
#After that you will do type in command promt like this python fillename.py


# In[14]:


#In Python, Updation or deletion of characters from a String is not allowed. 
#This will cause an error because item assignment or item deletion from a String is not supported. 
#Although deletion of entire String is possible with the use of a built-in del keyword. 
#This is because Strings are immutable, hence elements of a String cannot be changed once it has been assigned. 
#Only new strings can be reassigned to the same name.


# In[ ]:





# In[15]:


#Data Types
#numbers,strings,list,tuples,dictionary
#numbers
a=10
print(a)


# In[16]:


#string
a="hello oba"
print(a)


# In[17]:


print('oba')


# In[18]:


b = '50'
print(b)


# In[19]:


print(a*3)


# In[20]:


#slice operator
a = "hello oba"
print(a[0:6])
print(a[4:8])
print(a[0:9])
print(a[5:])


# In[21]:


print(a[0])


# In[22]:


#To print separete lines
a="hello    oba"
print(a)


# In[23]:


a='''hello
oba
how
are 
you'''
print(a)


# In[24]:


#List is used to store more than 1 value 
#Here used to open braket symble[]
a = [10]
print(type(a))


# In[25]:


c=[10,3.255,"oba"]
print(c)
print(type(c))
print(c*5)


# In[26]:


#List is a mutable(it will be changeble)


# In[27]:


#Tuple is a imutable(it is not changble)
#here used to paranthasis symble()
a=(12,5.22,"oba")
print(a)
print(a[0:5])
print(a[3:])
print(type(a))


# In[28]:


#Python Dictionary
#Last Updated: 14-06-2020 
#Dictionary in Python is an unordered collection of data values, 
#used to store data values like a map, which unlike other Data Types that hold only single value as an element,
#Dictionary holds key:value pair. Key value is provided in the dictionary to make it more optimized. 
#Note – Keys in a dictionary doesn’t allows Polymorphism.
#Creating a Dictionary
#In Python, a Dictionary can be created by placing sequence of elements within curly {} braces, separated by ‘comma’. 
#Dictionary holds a pair of values, one being the Key and the other corresponding pair element being its Key:value.
#Values in a dictionary can be of any datatype and can be duplicated, whereas keys can’t be repeated and must be immutable. 
#Note – Dictionary keys are case sensitive, same name but different cases of Key will be treated distinctly.
 


# In[29]:


#Dictionary if you store key ,value pair to use dictionary
#dictionary(key : value)
#Here used to curly brakets{}
#Dictionary is a
f={'name':'oba','age':25,'sex':'male'}
print(type(f))
print(f)
print(f.keys())
print(f.values())
print("\nDictionary with the use of Mixed Keys: ") 


# In[30]:


Dict= {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict)


# In[31]:


#Python Sets
#Last Updated: 20-11-2019 
#In Python, Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements.
#The order of elements in a set is undefined though it may consist of various elements.
#The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking- 
#-whether a specific element is contained in the set.

#Creating a Set
#Sets can be created by using the built-in set() function with an iterable object or a sequence -
#-by placing the sequence inside curly braces, separated by ‘comma’.
#Note – A set cannot have mutable elements like a list, set or dictionary, as its elements.


# In[32]:


set1 = set() 
print("Intial blank Set: ") 
print(set1) 
  


# In[33]:



# Creating a Set with  
# the use of a String 
set1 = set("GeeksForGeeks") 
print("\nSet with the use of String: ") 
print(set1) 
  


# In[34]:


set2 = set("THAMMISETTI OBULESU")
print(set2)


# In[35]:


# Creating a Set with 
# the use of Constructor 
# (Using object to Store String) 
String = 'GeeksForGeeks'
set1 = set(String) 
print("\nSet with the use of an Object: " ) 
print(set1) 
  


# In[36]:


oba = 'thammisetti obulesu'
set3 = set(oba)
print(set3)


# In[37]:


oba2 = "Thammisetti obulesu"
string = set(oba2)
print(string)


# In[38]:


# Creating a Set with  
# a List of Numbers 
# (Having duplicate values) 
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5]) 
print("\nSet with the use of Numbers: ") 
print(set1) 


# In[39]:


se = set([1,3,5,6,2,1,4,5,6,7,8,9,8,7,9])
print(se)


# In[40]:



# Creating a Set with  
# a mixed type of values 
# (Having numbers and strings) 
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']) 
print("\nSet with the use of Mixed Values") 
print(set1)


# In[41]:


sets = ([1,6,5,5,6,6,'oba',2,2,'babu'])
print(sets)


# In[42]:


# Python program to demonstrate  
# Addition of elements in a Set 
  
# Creating a Set 
set1 = set() 
print("Intial blank Set: ") 
print(set1) 
  


# In[43]:


# Adding element and tuple to the Set 
set1.add(8) 
set1.add(9) 
set1.add((6,7)) 
print("\nSet after Addition of Three elements: ") 
print(set1) 


# In[44]:


set1.add("oba")
set1.add(55)
set1.add(22)
print(set1)


# In[45]:


# Adding elements to the Set 
# using Iterator 
for i in range(1, 6): 
    set1.add(i) 
print("\nSet after Addition of elements from 1-5: ") 
print(set1) 


# In[46]:


set4=set()
print(set4)


# In[47]:


for i in range(1, 8):
    set4.add(i)
print(set4)


# In[48]:


#Using update() method
#For addition of two or more elements Update() method is used. 
#The update() method accepts lists, strings, tuples as well as other sets as its arguments.
#In all of these cases, duplicate elements are avoided.


# In[49]:


# Python program to demonstrate  
# Addition of elements in a Set 
  
# Addition of elements to the Set 
# using Update function 
set1 = set([ 4, 5, (6, 7)]) 
set1.update([10, 11]) 
print("\nSet after Addition of elements using Update: ") 
print(set1) 


# In[50]:


set5 = set()
print(set5)


# In[51]:


set1 = set([ 5,6, (5, 6)])
set1.update([9, 10])
print(set1)


# In[52]:


set5 =set()
print(set5)


# In[53]:


# Python program to demonstrate 
# Accessing of elements in a set 
  
# Creating a set 
set5 = set(["Geeks", "For", "Geeks"]) 
print("\nInitial set") 
print(set5)


# In[54]:


set6 = set (["oba", "age", "oba"])
print(set6)


# In[55]:


for i in set6:
    print(i, end=" ")


# In[56]:


#Removing elements from using set1.remove()
set6 = set([2, 2, 3, (5, 5)])
print(set6)


# In[57]:


set6.remove(3)
print(set6)


# In[58]:


set1 = set([1, 2, 3, 4, 5, 6,  
            7, 8, 9, 10, 11, 12]) 
print("Intial Set: ") 
print(set1) 
  


# In[59]:


# Removing elements from Set 
# using Remove() method 
set1.remove(5) 
set1.remove(6) 
print("\nSet after Removal of two elements: ") 
print(set1) 
  


# In[60]:



# Removing elements from Set 
# using Discard() method 
set1.discard(8) 
set1.discard(9) 
print("\nSet after Discarding two elements: ") 
print(set1) 
  


# In[61]:


# Removing elements from Set 
# using iterator method 
for i in range(1, 5): 
    set1.remove(i) 
print("\nSet after Removing a range of elements: ") 
print(set1) 


# In[62]:



# Creating a Nested Dictionary  
# as shown in the below image 
Dict = {1: 'Geeks', 2: 'For',  
       3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}} 
 
print(Dict)  


# In[63]:


dicct = {1: 'oba', 2: 'oba1',
        3:{"oba" : "oba3"}}
print(dicct)


# In[64]:


Dict[0] = "oba"
Dict[1] = "nag"
Dict[2] = "satya"
print(Dict)


# In[65]:


Dict[6] = "raj"
Dict[7] = "babu"
print(Dict)


# In[66]:



# Creating a Dictionary  
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
 
# accessing a element using get() 
# method 
print("Accessing a element using get:") 
print(Dict.get(3)) 


# In[67]:


#Python Operators

#Operators are used to perform operations on variables and values.
#Python divides the operators in the following groups:
    #Arithmetic operators
    #Assignment operators
    #Comparison operators
    #Logical operators
    #Identity operators
    #Membership operators
    #Bitwise operators


# In[68]:


#Python Arithmetic Operators
#Arithmetic operators are used with numeric values to perform common mathematical operations:

#Example
#+
#Addition
a = 10
b = 50
print(a + b)
#-
#Subtraction
print(a-b)
#*
#Multiplication
print(a*b)
#/
#Division
print(b/a)
#%
#Modulus
print(b%a)
#**
#Exponentiation
print(b**a)
#//
#Floor division
print(a//b)


# In[69]:


#If you use cube 
print(2*2*2)
print(2**3)


# In[70]:


#Python Assignment Operators


#Assignment operators are used to assign values to variables:

#Example
#=
x = 5
print(x)
#+=
a += 3
a = a + 3
print(a)
#-=
b -= 3
b = b - 3
print(b)
#*=
c = 3
c *= 3
print(c)
#/=
d = 3
d /= 3
d = d / 3
print(d)
#%=
e = 3
e %= 3
e = e % 3
print(e)
#//=
f = 3
f //= 3
f = f // 3
print(f)
#**=
g = 3
g **= 3
g = g ** 3
print(g)
#&=
h = 3
h &= 3
h = h & 3
print(h)
#|=
i = 3
i |= 3
i = i | 3
print(i)
#^=
j = 3
j ^= 3
j = j ^ 3
print(j)
#>>=
k = 3
k >>= 3
k = k >> 3
print(k)
#<<=
l = 3
l <<= 3
l = l << 3
print(l)


# In[71]:


#Python Membership Operators

#Membership operators are used to test if a sequence is presented in an object:

#Example
#in 
    #Returns True if a sequence with the specified value is present in the object
a = 10
b = 25
list = [1, 12, 10, 15, 20]
if a in list:
    print("a is in the true")
else:
    print("a is not in the true")

#not in
    #Returns True if a sequence with the specified value is not present in the object
if b not in list:
    print("b is not in the result is true")
else:
    print("b is in the result is true")


# In[72]:


#Python Identity Operators:

#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object,
#with the same memory location:

#is 
#Returns True if both variables are the same object
a = 20
b = 20
if (a is b):
    print("both are same")
else:
    print("both are different")


# In[73]:


#is not
#Returns True if both variables are not the same object
a = 20
b = 12.02
if (a is b):
    print("both are same")
else:
    print("both are different")
if (a is not b):
    print("both are same")
else:
    print("both are different")


# In[74]:


#Python Bitwise Operators:

#Bitwise operators are used to compare (binary) numbers:

#&(ampercent symbol) 
#AND
#Sets each bit to 1 if both bits are 1
a = 10
b = 5
c = a & b
print(c)
#OR
#Sets each bit to 1 if one of two bits is 1
c = a | b
print(c)


# In[75]:


#Python Comparison Operators:

#Comparison operators are used to compare two values:
#Operator
#==
#Equal
x == 10
if x==10:
    print("value is 10")

#!=
#Not equal

if x != 10:
    print("true")

if x != 20:
    print("true")
else:
    print("false")
#>
#Greater than
if x > 50:
    print("true")
else:
    print("false")

#<
#Less than
if x < 5:
    print("true")
#>=
#Greater than or equal to
if x >= 10:
    print("true")
else:
    print("false")
#<=
#Less than or equal to
if x <= 120:
    print("true")
else:
    print("false")


# In[76]:


#Python Logical Operators:

#Logical operators are used to combine conditional statements:

#and 
#Returns True if both statements are true
x < 5 and  x < 10
p
or
Returns True if one of the statements is true
x < 5 or x < 4
Try it »
not
Reverse the result, returns False if the result is true
not(x < 5 and x < 10)


# In[ ]:


#Python Conditions and If statements
#Python supports the usual logical conditions from mathematics:
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b
#These conditions can be used in several ways, most commonly in "if statements" and loops.
#An "if statement" is written by using the if keyword.


# In[77]:


obaage = 25
if obaage == 25:
    print("real age")


# In[78]:


num = 30
if num%3==0:
    print("is correct")
else:
    print("wrong")


# In[79]:


num = 50
if num%5==10:
    print("if correct")
else:
    print("wrong")


# In[80]:


a,b,c = 20, 30, 50
if a>b and b > c:
    print("correct")
else:
    print("wrong")


# In[81]:


x,y = 50,20
if x>y:
    print("correct")


# In[82]:


#Indentation:

#Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
#Other programming languages often use curly-brackets for this purpose.
a,b = 20,50
if a > b:
print("correct")


# In[83]:


#Elif
#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 20
b = 100
if a > b:
    print("a greater then b")
elif a < b:
    print("a less than b")
else:
    print("correct")


# In[84]:


#Else
#The else keyword catches anything which isn't caught by the preceding conditions.
a = 100
b = 200
c = 120
if a > c:
    print("a greater than c")
elif a > c:
    print("c greater than b")
else:
    print("same")


# In[85]:


#Nested If
#You can have if statements inside if statements, this is called nested if statements.
a = 2009
b = 300
if a > b:
    print("is correct")
    if b < a:
        print("this is also correct")
else:
    print("all correct")


# In[86]:


#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content,
#put in the pass statement to avoid getting an error.
a = 10
if a == 20:
    pass


# In[87]:


#Python Loops
#Python has two primitive loop commands:
#while loops
#for loops


# In[88]:


#Python For Loops
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, and works more like an iterator method as found -
#-in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.


# In[89]:


number = 10
for number in range(1,20):
    print(number)


# In[90]:


names = ["oba","nag","umar"]
for x in names:
    print(names)


# In[91]:


names = ["nag","oba"]
for x in names:
    print(x)


# In[92]:


#Looping Through a String
#Even strings are iterable objects, they contain a sequence of characters:
for x in "oba":
    print(x)


# In[93]:


#The break Statement
#With the break statement we can stop the loop before it has looped through all the items:

names = ["oba","nag","babu"]
for x in names:
    print(x)
    if x == "hari":
        break


# In[94]:


age = [20, 25, 30, 35]
for x in age:
    print(x)
    if x == 20:
        break


# In[95]:


a = ["lakshmi","oba","malli"]
for x in a:
    if x == "oba":
        print(x)


# In[96]:


a = ["lakshmi","oba","malli"]
for x in a:
    if x == "oba":
        break
    print(x)


# In[97]:


#The continue Statement
#With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruit = ["banana","apple","orange"]
for x in fruit:
    if x == "banana":
        continue
    print(x)


# In[98]:


age = [20, 30, 40]
for x in age:
    if x == 20:
        continue
    print(x)


# In[100]:


#Else in For Loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(1, 9):
    print(x)
else:
    print("finsh")


# In[99]:


#Nested Loops
#A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop":

age = [15, 25, 30, 40]
name = ["oba","nag","raj","abhi"]
for x in age:
    for y in name:
        print(x, y)


# In[101]:


age = [20,50]
name = ["rajgopal","remo"]
for x in age:
    for y in name:
        print(x, y)


# In[102]:


#The while Loop
#With the while loop we can execute a set of statements as long as a condition is true.
a = 2
while a<10:
    print(a)
    a=a+1


# In[103]:


num = 15
while num < 20:
    print(num)
    num = num+1


# In[104]:


num = 0
while num < 20:
    num = num+1
    if num == 10:
        continue
    print(num)


# In[ ]:


a = 1
while a / 10:
    a = a+2
    if a > 10:
        
        continue
    print(a)
    


# In[4]:


i = 1
while i < 6:
    i = i+1
    if i == 3:
        break
    print(i)
  
    


# In[6]:


#Number in  deeply
#abs it will give positive number
print(abs(-12))


# In[9]:


#mathematical expressition
import math  # it is preedefined function
print(math.exp(2))


# In[11]:


import math
print(math.exp(12))


# In[13]:


import math
print(math.exp(100.2))


# In[15]:


#ceil
#it will give round up value
print(math.ceil(46.22))


# In[17]:


print(math.ceil(12.333))


# In[18]:


print(math.ceil(45.33))


# In[20]:


#floor it wiil give exact value even having a float number
print(math.floor(46.222))


# In[22]:


#power
print(math.pow(10,2))


# In[24]:


print(math.pow(11,2))


# In[27]:


#Square root
print(math.sqrt(2))


# print(math.sqrt(23))

# In[29]:



print(math.sqrt(23))


# In[31]:


print(max(20,50,78))


# In[33]:


print(min(20,25,310))


# In[36]:


#Random
import random
tuple = (10, 20, 30, 45, 56)
print(random.choice(tuple))


# In[40]:


print(random.choice(tuple))


# In[43]:


print(random.choice(tuple))


# In[45]:


print(random.random())


# In[47]:


print(random.random())


# In[50]:


print(random.random()*100)


# In[52]:


print(random.randrange(1,11))


# In[54]:


print(random.randrange(1,11,2))


# In[57]:


print(random.uniform(2,10))


# In[59]:


print(random.uniform(2,10))


# In[61]:


print(random.uniform(2,10))


# In[63]:


print(random.uniform(2,10))


# In[2]:


#Strings are Arrays
#Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
#However, Python does not have a character data type, a single character is simply a string with a length of 1.
#Square brackets can be used to access elements of the string.
name = "Thammisetti obulesu"
name2 = "Thammisetti Nagarjuna"
print(name + name2)


# In[4]:


name = "Thammisetti obulesu"
print(name[0:2])


# In[7]:


print(len(name))


# In[9]:


#replication factor
print(name*5)


# In[14]:


name = 'obu'
print(name.capitalize())


# In[17]:


print(name.count(name))


# In[20]:


nnn = "t"
print(name.count(nnn))


# In[24]:


name3 = "Thammisetti obulesu"
print(name3[-6:-4])


# In[26]:


print(name3[-5:-2])


# In[30]:


#String Length
#To get the length of a string, use the len() function.
hi = "Thammisetti obulesu"
print(len(hi))


# In[35]:


n = "12345 thammisetti obulesu"
print(len(n))


# In[41]:


nam = "Thammisetti"
print(name.find(nam))


# In[46]:


#Alphanumaric method
name = "oba"
print(name.isalnum())


# In[48]:


name = "obulessu234"
print(name.isalnum())


# In[50]:


name = "oba@9398"
print(name.isalnum())


# In[52]:


name = "oba2"
print(name.isdigit())


# In[53]:


name = "oba"
print(name.isalpha())


# In[55]:


name = "9398605349"
print(name.isdigit())


# In[57]:


name = "oba"
print(name.islower())


# In[61]:


name = "Oba"
print(name.islower())
print(name.isupper())


# In[64]:


name = "OBULESU"
print(name.isupper())
print(name.lower())


# In[66]:


name= "obulesu"
print(name.upper())


# In[67]:


#swapcase
#it is used to change the lower case to upper case
name = "pbiOOB"
print(name.swapcase())


# In[2]:


#List its methods
list = [2,"oba",2.33]
print(list)


# In[6]:


data = [2,"oba2",2.22,"amma"]
data1 = [3,"nag",55.21,"malli"]
print(data + data1)


# In[8]:


print(data*4)


# In[11]:


data = [2,3,5,"oba"]
for data in range(1,2):
    if data == 5:
        continue
    print(data)


# In[15]:


data = ["oba",1,2,"nagarjuna"]
print(data[1:5])


# In[17]:


#updating method
data[0] = "obulesu"
print(data)


# In[19]:


data[2] = 5
print(data)


# In[21]:


#append method
data.append("hydrabad")
print(data)


# In[23]:


data.append("simhadripuram")
print(data)


# In[25]:


#Deleting method
del data[5]
print(data)


# In[27]:


del data[4]
print(data)


# In[29]:


print(len(data))


# In[34]:


tuple = (1,22,33,55,42)
print(max(tuple))
print(min(tuple))


# In[44]:


#count : It is used to find out how many multipule times to present the given list of the number
list = [10,12,14,32,12,44,10]
print(list)
print(list.count(12))


# In[46]:


print(list.count(14,12))


# In[49]:


print(list.index(12))


# In[51]:


list.insert(4,100)
print(list)


# In[53]:


list.reverse()
print(list)


# In[55]:


#sort method
list.sort()
print(list)


# In[57]:


list.sort()
list.reverse()
print(list)


# In[59]:


#tuples it's methods this is immutable objects
tuple = (12,14,22,4.5,"oba")
print(tuple)


# In[61]:


#slicing operator:
print(tuple[2:4])


# In[63]:


print(tuple[3:])


# In[65]:


#replication factor:
print(tuple*4)


# In[67]:


#length method:
print(len(tuple))


# In[72]:


#max,min
tuple = (22,45,22544,34,10.2,23,55,55,85,23)
print(max(tuple))


# In[74]:


print(min(tuple))


# In[78]:


#count
print(tuple.count(10.2))


# In[81]:


#dictionary its methods:
dic = {"name":"oba",}
print(dic)


# In[84]:


dic["name"] = 'nag'
print(dic)


# In[121]:


dic["name"] = "obulesu"
print(dic)


# In[89]:


print(len(dic))


# In[120]:


print(dic.keys())


# In[93]:


print(dic.values())


# In[95]:


print(dic.items())


# In[98]:


#clear method:
dic.clear()


# In[100]:


print(dic)


# In[2]:


#copy:
dic1 = {"id":12345}
dic2 = dic1.copy()
print(dic2)


# In[3]:


print(dic2)


# In[5]:


#Time and Date and Calender:
import time


# In[7]:


t1 = time.localtime(time.time())
print(t1)


# In[10]:


t2 = time.asctime(time.localtime(time.time()))
print(t2)


# In[117]:


import calendar
c1 = calendar.month(2021,8,12)
print(c1)


# In[118]:


c1 = calendar.prcal(2021)
print(c1)


# In[7]:


print(calendar.isleap(2020))


# In[9]:


print(calendar.isleap(2017))


# In[11]:


c2=calendar.month(2017,8)
print(c2)


# In[17]:


c2=calendar.prcal(2020)
print(c2)


# In[5]:


#functions
#This is used to block of code write oncwe and exicute more times
def oba(a,b):
    t=a+b
    print("total is:",t)


# In[22]:


oba(10,2)


# In[3]:


def total(x,y):
    sum=x+y
    print(sum)


# In[4]:


total(100,200)


# In[9]:


def oba3(x,y):
    sum=x+y
    print(sum)


# In[11]:


oba3(20,30)


# In[12]:


def ooo(a,b,c):
    ok=(a+b-c)
    print(ok)


# In[15]:


ooo(20,30,60)


# In[17]:


import time
t1=time.localtime(time.time())
print(t1)


# In[20]:


t1=time.asctime(time.localtime(time.time()))
print(t1)


# In[22]:


import calendar


# In[24]:


c1=calendar.month(2017,10)
print(c1)


# In[26]:


c1=calendar.prcal(2020)
print(c1)


# In[6]:


oba=input("Hi this is:")
print("name:",oba)


# In[4]:


i=int(input("my age is:"))
print("age:",i)


# In[6]:


j=float(input("my weight is:"))
print("weight:",j)


# In[8]:


#input user data 
#this is shows the user data to output
name=input("my namae is:")
print("name:",name)
age=input("my age is:")
print("age:",age)
weight=input("my weight is:")
print("age:",age)


# In[14]:


#file handilin
#here open,close,read,write
#this is all use to create file in our local drives
#And read the files
obj=open("e:/filehandling.txt","w")
obj.write("Hi oba how are you")
obj.close()


# In[17]:


obj=open("e:/filehandling.txt","r")
s = obj.read()
print(s)


# In[20]:


f=open("e:/file.csv","w")
f.write("hi babu this is my new job and also my new project")
f.close()


# In[23]:


f=open("e:/file.csv","r")
s=f.read()
print(s)
f.close()


# In[26]:


f=open("e:/file2.json","w")
f.write("fine ra where are you")
f.close()


# In[29]:


f=open("e:/file2.json","r")
s=f.read()
print(s)


# In[32]:


f=open("e:/fileszie.tet","w")
f.write("umar")
f.close()


# In[34]:


f=open("e:/fileszie.tet","r")
s=f.read()
print(s)


# In[36]:


f=open("E:/fileresume.txt","r")
s=f.read()
print(s)


# In[39]:


f=open("E:/covid_19_india (1).csv","r")
s=f.read()
print(s)


# In[47]:


q=open("e:/umar.json","w")
q.write("helli my name is umar")
q.close()


# In[48]:


q=open("e:/umar.json","r")
s=q.read()
print(s)


# In[55]:


h=open("E:/file2.JSON","r")
s=h.read()
print(s)


# In[57]:


k=open("e:/obu.txt","w")
k.write("python practice")


# In[59]:


k.close()


# In[61]:


k=open("e:/obu.txt","a")
k.write("by thammisetti obulesu")


# In[63]:


k.close()


# In[68]:


k=open("e:/obu.txt","r")
s=k.read()
print(s)
k.close()


# In[71]:


#Rename method
import os
os.rename("e:/obu.txt","e:/obulesu.txt")


# In[75]:


import os
os.rename("e:/fileresume.txt","e:/resumesss.txt")


# In[78]:


os.remove("e:/obulesu.txt")


# In[80]:


print(os.getcwd())


# In[9]:


#create a folder
import os
os.mkdir("E:/2")


# In[84]:


#present working directory
print(os.getcwd())


# In[86]:


#change directory
os.chdir("e:/india")


# In[10]:


print(os.getcwd())


# In[91]:


os.mkdir("e:/india2")


# In[94]:


#removie diretory
os.rmdir("e:/india2")


# In[1]:


#module
#nothing but different tasks
#your project will be categarized into multiple file
#after that import to and excute to program
import display1
display1.msg1()


# In[4]:


from datetime import datetime


# In[10]:


print(datetime.now())


# In[15]:


from math import sqrt,tan


# In[17]:


print(sqrt(100))
print(tan(45))


# In[20]:


def oba():
    print("ok")
oba() #here calling


# In[23]:


def div(x,y):
    print(x/y)
div(10,2)# here (10,2) is posititonal arguments


# In[25]:


div(15,5)


# In[27]:


def mult(x,y):
    print(x*y)
mult(10,3)


# In[29]:


mult(10,3)


# In[37]:


def manage(name,age):
    x = "my name is:"+name
    y = "my age is:"+str(age)
    return x,y


# In[39]:


manage("oba",25)


# In[41]:


manage("nagarjuna",23)


# In[49]:


def allow(*a):
    x = str(a)
    return x


# In[53]:


allow("jp",25,2355,23.56)


# In[58]:


a = "oba"
print(a.capitalize())


# In[60]:


print(a.lower())


# In[ ]:




