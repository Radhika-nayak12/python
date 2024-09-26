# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangable (set items are unchangable, but you can remove items and add mew items), no duplication and unindexed.
# Set are written with curly brackets.

# it is a mathematical concept in discretemultiset har element ki multiplicity nikali jati hai 




# this = {'apple','banana','cherry'}
# print(this)



# A set can contain different data types
# thisset = {'cherry',True,1,2}   = this set len is 3 because it is taking 1 and true as 1
# thiset = {'cherry',True,3,2.2}
# print(type(thiset))
# print(thiset)

# print(len(thiset))

# set = {"apple","banana","cherry"}
# for x in set:
#     print(x)    
# output = 
# cherry
# apple
# banana

# thisset = {"apple","banana","cherry"}
# print("banana" in thisset)  = True

# thisset = {"apple","banana","cherry"}
# print("orange" in thisset)   = False


# thisset = {"apple","banana","cherry"}
# thisset.add("o")
# print(thisset)

# output = {'banana', 'o', 'apple', 'cherry'}

# set = {"apple","banana","cherry"}
# t = {"pineapple","mango","papaya"}
# set.update(t)
# print(set)

# output = {'cherry', 'banana', 'papaya', 'pineapple', 'mango', 'apple'}

# set.remove("banana")
# print(set)

# output = {'cherry', 'papaya', 'apple', 'pineapple', 'mango'}

# if the item to remove does not exist, remove() will raise an error

# set = {"apple","banana","cherry"}
# set.discard("b")
# print(set)

# discard() will not raise an error

# set = {"apple","banana","cherry"}
# x = set.pop()
# print(x)

# set = {"apple","banana","cherry"}
# set.clear()
# print(set)

# set = {"apple","banana","cherry"}
# del set
# print(set)  output = <class 'set'>

# x = {"apple",'cherry','banana'}
# del x
# print(x)

# dictio= {"apple",'cherry','banana'}
# del dictio
# print(dictio)


# set1 = {'a','b','c'}
# set2 = {1,2,3}
# set3 = set1.union(set2)
# print(set3)
# output = {'c', 1, 2, 3, 'b', 'a'}



# set1 = {'a','b',3}
# set2 = {1,2,3}
# set3 = set1.union(set2)
# print(set3)

# output = {1, 2, 3, 'b', 'a'}


# x = {"apple","banana","cherry"}
# y = {"google","microsoft","apple"}
# z = x.intersection(y)
# print(z) =  {'apple'}

# z = x.symmetric_difference(y)
# print(z)     =  {'google', 'cherry', 'banana', 'microsoft'}


# x = {"apple","banana","cherry",True}
# y = {"google",1,"apple",2}
# z = x.symmetric_difference(y)
# print(z)  =   {2, 'banana', 'google', 'cherry'}


     