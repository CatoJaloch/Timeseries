#if you want to run a specific part of the code,comment the rest out
#** Indexing in Python
# string
x = 'frog'
print(x[1])


# list
y= 'pig','dog','cat'
print(y[2])

# tuple
z = 'cow','horse','sheep'
print(z[0]) 

# r
# cat
# cow

# slicing slice out substrings,sublists,subtuples using indexes [start:end+1:step]
x= 'computer' 
print(x[1:4]) # omp...the start is inclusive and the end is exclusive
print(x[:4]) # comp...if the start is not specified, it starts from the beginning
print(x[4:]) # uter...if the end is not specified, it goes until the end
print(x[-4:]) # uter...negative indexing starts from the end
print(x[1:6:2]) #opt...the step is 2 so ..the end +1 is e so we take op and t
print(x[:-1]) # compute...if the step is negative, it goes backwards
print(x[::-1]) # retupmoc...if the step is negative and the start and end are not specified, it reverses the string

# adding/concatenating - combining 2 sequences of the same type using +
# string
x = 'horse'+ 'shoe'
print(x)
#list 
y=['pig','cat']+['cow','sheep']
#tuple 
z=('horse', 'shoe')+('pig','cat')

# multiplying - repeating a sequence a certain number of times using *
#string
x = 'coyg' * 7 # coygcoygcoygcoygcoygcoygcoyg
print(x)
# list
y = ['pig','cat'] * 3 # ['pig', 'cat', 'pig', 'cat', 'pig', 'cat']  
print(y)
# tuple
z = ('horse', 'shoe') * 2 # ('horse', 'shoe', 'horse', 'shoe')
print(z)      

#checking membership- whether an item is or isnt in a sequence
x = 'dog'
print('u' in x)

y =['pig','cat','cow']
print('cow' not in y) # False

z =('rat','horse','shoe')
print('rat' in z) # True

# iterating through items in a sequence
# item
x =['rat','dog','cat','cow']
for item in x:
    print(item)
#index and item
y = ['4','7','8']
for index,item in enumerate (y):
    print(index,item)

#number of items in a sequence/counting items in a sequence
x = 'bug'
print(len(x)) #3

# minimum and maximum items in a sequence
x = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(min(x)) # 1
print(max(x)) # 9
 
y ='Cato'
print(min(y)) # 'C'...the minimum is determined by the ASCII value of the characters
print(max(y)) # 't'...the maximum is determined by the ASCII value of the characters 

# sorting items in a sequence
x = ('10', '2', '3', '4', '5')
print(sorted(x)) # ['10', '2', '3', '4', '5']...the sorting is done based on the ASCII value of the characters, so '10' comes before '2' because '1' comes before '2' in the ASCII table    

print (sorted(x, key=int)) # ['2', '3', '4', '5', '10']...the sorting is done based on the integer value of the characters, so '2' comes before '10' because 2 is less than 10

# sorting,,,returns  a new list of items in sorted order , but does not change the original list
# string
x = 'bug'
print(sorted(x)) # ['b', 'g', 'u']...the sorting is done based on the ASCII value of the characters

# list
y = ['pig','cat','cow']
print(sorted(y)) # ['cat', 'cow', 'pig']...the sorting is done based on the ASCII value of the characters

# sorting by the second character of the string
# add a ket parameter and a lambda function to return second chrter
z = ['rat','dig','cut','cow'] 
print(sorted(z, key=lambda x: x[1])) #['rat', 'dig', 'cow', 'cut']...the sorting is done based on the second character of the string, so 'cut' comes before 'cow' because 'u' comes before 'o' in the ASCII table

#Count of an item in a sequence
#string
x = 'dived'
print(x.count('d')) #2 beacause there are 2 'd's in the string

#list
y = ['dio','hflkw','sgrj']
print (y.count('dio')) #1 because there is 1 'dio' in the list

#index of an item in a sequence
#string
x = 'dived'
print(x.index('v')) #2 because v is on the 2nd index of the string
#list
y = ['dio','hflkw','sgrj','dio']
print(y.index('dio')) #0 because the index method returns the index of the first occurrence of the item in the list, so it returns 0 because 'dio' is on the 0th index of the list

#unpacking the n items of a sequence into n variables
x =['ret','dog','cat']
a,b,c =x
print(a,c) # ret cat...the first item of the list is assigned to a and the second item is assigned to b and the third item is assigned to c

#LISTS
# General purpose most widely used can grow and shrink in size, can contain items of different types, mutable (can be changed after creation)

# constructors...creating new lists using the list() constructor
x=list() # creates an empty list
y = ['a',25,'dog'] # creates a list with 3 items of different types
tuplel = (10,20)# creates a list from a tuple
z = list(tuplel) # creates a list from a tuple

#,list comprehension...creating new lists using a concise syntax
a = [m for m in range(8)] 
print(a) # [0, 1, 2, 3, 4, 5, 6, 7]...the list comprehension creates a new list by iterating over the range of numbers from 0 to 7 and adding each number to the list
b = [i**2 for i in range(10) if i>4] 
print(b) # [25, 36, 49, 64, 81]...the list comprehension creates a new list by iterating over the range of numbers from 0 to 9, squaring each number, and adding it to the list if the number is greater than 4

# delete - delete a list r an item in a list
x= [5,4,6,3,2,1]
del(x[0]) # deletes the first item of the list, so the list becomes [4,6,3,2,1]
del(x) # deletes the entire list

#append
x = [5,4,6,3,2,1]
x.append(23) # adds 23 too the list so it becomes [5,4,6,3,2,1,23]
print(x)

# extend
x =[1,2,3,4,5]
y =[6,7,8,9,10]
x.extend(y) # adds the items of y to x so it becomes [1,2,3,4,5,6,7,8,9,10]
print(x)

#insert an item at a given index
t = [1,3,4,5,6]
t.insert(1,2) # inserts 2 at index 1 so the list becomes [1,2,3,4,5,6]
print(t)
t.insert(1,['we','will']) # inserts ['we','will'] at index 1 so the list becomes [1,['we','will'],2,3,4,5,6]
print(t)

#pop -pops last item off list and returns item
x = [1,2,3,4,5]
x.pop() # removes the last item of the list and returns it, so it returns 5 and the list becomes [1,2,3,4]
print(x)

#remove - removes the first occurrence of an item in a list
p = [1,2,3,4,5,2]
print(p.remove(2)) # removes the first occurrence of 2 in the list, so it removes the first 2 and the list becomes [1,3,4,5,2]

#reverse - reverses the items in a list
x = [1,2,3,4,5]
print(x.reverse()) # reverses the items in the list, so it becomes [5,4,3,2,1]

#TUPLES
#similar to lists but immutable (cannot be changed after creation) and are created using parentheses instead of square brackets
# constructors...creating new tuples using the tuple() constructor

x = ()
x = (1,2,3)
x = 1,2,3
x = 2, # comma tells python it is a tuple even if there is only one item
print(x,type(x))

y =([1,2],3,4) # tuple with a list in index 0
del(y[0][1]) # deletes the second item of the list in index 0 of the tuple, so the tuple becomes ([1],3,4)
print(y) # ([1], 3, 4)

#SETS
#stores non duplicate items in an unordered way, mutable (can be changed after creation), created using curly braces or the set() constructor
# constructors...creating new sets using the set() constructor

x = {3,5,3,5}
print(x) # {3, 5}...the set only stores unique items, so it removes the duplicate 3 and 5

y = set()
print(y) # set()...the set() constructor creates an empty set

listl = [1,2,3,4,5]
z = set(listl) # creates a set from a list
print(z) # {1, 2, 3, 4, 5}

# set operations
x = {3,8,5}
print(x)
x.add(7) # adds 7 to the set, so it becomes {3, 5, 7, 8}
print(x)
x.remove(3) # removes 3 from the set, so it becomes {5, 7, 8}
print(x)

# mathematical set functions
s1 = {1,2,3}
s2 = {3,4,5}
print(f"{s1 & s2}") # {3}...the intersection of s1 and s2 is the set of items that are in both sets, so it is {3}
print(f"{s1 | s2}") # {1, 2, 3, 4, 5}...the union of s1 and s2 is the set of items that are in either set, so it is {1, 2, 3, 4, 5}
print(f"{s1 - s2}") # {1, 2}...the difference of s1 and s2 is the set of items that are in s1 but not in s2, so it is {1, 2}
print(f"{s1 ^ s2}") # {1, 2, 4, 5}...the symmetric difference of s1 and s2 is the set of items that are in either set but not in both sets, so it is {1, 2, 4, 5}
print(f"{s1 <= s2}") # False...s1 is not a subset of s2 because it contains items that are not in s2
print(f"{s1 >= s2}") # False...s1 is not a superset of s2 because it does not contain all the items in s2

#DICTIONARIES--DICT
#Key value pairs,unordered,mutable (can be changed after creation), created using curly braces or the dict() constructor

x = {'pork':25.3,'beef':33.8,'chicken':18.5}
print(x) # {'pork': 25.3, 'beef': 33.8, 'chicken': 18.5}...the dictionary stores key value pairs, so it is {'pork': 25.3, 'beef': 33.8, 'chicken': 18.5}    
#or
x = dict([('pork',25.3),('beef',33.8),('chicken',18.5)])
print(x) # {'pork': 25.3, 'beef': 33.8, 'chicken': 18.5}...the dict() constructor creates a dictionary from a list of key value pairs, so it is {'pork': 25.3, 'beef': 33.8, 'chicken': 18.5}

#dictionary operations
x ['lamb'] = 38.2 #add or update a key value pair in the dictionary, so it becomes {'pork': 25.3, 'beef': 33.8, 'chicken': 18.5, 'lamb': 38.2}
print(x)
del(x['pork']) # deletes the key value pair with the key 'pork'
print(x) # {'beef': 33.8, 'chicken': 18.5, 'lamb': 38.2}...the dictionary becomes {'beef': 33.8, 'chicken': 18.5, 'lamb': 38.2} after deleting the key value pair with the key 'pork'}
print(len(x)) # 3...the length of the dictionary is the number of key value pairs in the dictionary, so it is 3
print(x.keys()) # dict_keys(['beef', 'chicken', 'lamb'])
del(x) # deletes the entire dictionary 

#Accessing keys and values in a dict
y= {'pork':25.3,'beef':33.8,'chicken':18.5}
print(y.keys()) # dict_keys(['pork', 'beef', 'chicken'])...the keys() method returns a view object that displays a list of all the keys in the dictionary, so it is dict_keys(['pork', 'beef', 'chicken'])
print(y.values()) # dict_values([25.3, 33.8, 18.5])...the values() method returns a view object that displays a list of all the values in the dictionary, so it is dict_values([25.3, 33.8, 18.5])
print(y.items()) # dict_items([('pork', 25.3), ('beef', 33.8), ('chicken', 18.5)])...the items() method returns a view object that displays a list of all the key-value pairs in the dictionary, so it is dict_items([('pork', 25.3), ('beef', 33.8), ('chicken', 18.5)])

# check membership in y_keys (only looks in keys ,not values)
print('beef' in y.keys()) # True...the 'beef' key is in the dictionary, so it returns True
print(18.5 in y.values()) # True...the 18.5 value is in the dictionary, so it returns True  

#iterating a dictionary
for key in y:
    print(key) # pork beef chicken...the for loop iterates through the keys of the dictionary, so it prints pork beef chicken
    print(key , y[key]) # pork 25.3 beef 33.8 chicken 18.5...the for loop iterates through the keys of the dictionary and prints the key and its corresponding value, so it prints pork 25.3 beef 33.8 chicken 18.5


#PYTHON LIST COMPREHENSIONS
import random
#get values within a range
under_10 =[x for x in range(10)]
print('under_10:' + str(under_10)) # under_10:[0,1,2,3,4,5,6,7,8,9]

#getting squared values
squares = [x**2 for x in under_10]
print ('squares:'+ str(squares))

#getting odd numbers using mod
odds = [x for x in range(10) if x%2 == 1]
print ('odd nums:'+ str(odds))

#getting multiples of 10
ten_x = [x for x in range(10)] 
print ('ten_x:'+ str(ten_x)) # ten_x: [0,10,20,30,40,50,60...90]

#getting the index of a list item
names = ['Cosmo','Pedro','Anu','Ray']
idx = [k for k,v in enumerate(names) if v=='Anu']
print('index ='+str(index[0])) #index = 2

#delete an item from list
letters = [x for x in'ABCDEF']
random.shuffle(letters)
letrs = [a for a in letters if a!='C']
print(letters,letrs) 










