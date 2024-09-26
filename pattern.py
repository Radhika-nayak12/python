# 1
# 23
# 456

# n = int(input())
# for i in range(n):
#     for j in range(1,i+1):
#         print(i,end='')
#     print('')

# output

# 1
# 22
# 333
# 4444



# a = 1
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(a,end='')
#         a+=1
#     print('')

# output 

# 4
# 1
# 23
# 456

# 123
# 12
# 1

# a = n
# for i in range(n):
#     for j in range(1,a):
#         print(j,end='')
#     a-=1
#     print('')



# for i in range(n):
#     for j in range(n-i):
#         print(' ',end='')
#     for z in range(i+1):

#         print('*',end=' ')

#     print('')

# output 
# 4
#     * 
#    * * 
#   * * * 
#  * * * * 


#  * * * * 
#   * * * 
#    * * 
#     * 

# diamond and pascal triangle`

# Print Pascal's Triangle in Python


# n = 5

# for i in range(1, n+1):
#     for j in range(0, n-i+1):
#         print(' ', end='')


#     C = 1
#     for j in range(1, i+1):


#         print(' ', '*', sep='', end='')


#         C = C * (i - j) // j
#     print()

# output 

#       *
#      * *
#     * * *
#    * * * *
#   * * * * *




# Diamond star pattern
# n = int(input())

# upper
# for i in range(1, n+1):
#     for j in range(1,n-i+1):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
#     print()

# lower
# for i in range(n-1,0, -1):
#     for j in range(1,n-i+1):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
    # print()



# str=input2


# break code
# i = 0
# a = 'santabanta'
# while i < len(a):
#     if a[i] == 'n':
#         break
#     i += 1
# print('Current Letter :', a[i], i)


# continue code

# i = 0
# while i<6:
#     i+=1
#     if i == 3:
#         continue
#     print(i)


# i = 0
# while i<11:
#     i+=1
#     if i%3==0:
#         continue
#         print(i)

# n = int(input())
# for i in range(1,11):
#     if i%3==0:
#         continue
#     else:
#         print(i)

# t1 = ['abc',34,True,40.4,'male']
# print(type(t1))
# print(t1[3],t1[4])
# print(t1[::4])

# Insert()
# l1 = ['apple','banana','charry']
# l1.insert(2,'watermelon')
# print(l1)

# thislist = ['apple','banana','cherry']
# thislist[1] = 'orange'
# print(thislist)

# thislist = ['apple','banana','cherry','orange','kiwi','mango']
# thislist[1:3] = ['blackcurrent','watermelon']
# print(thislist)


# thislist = ['apple','banana','cherry']
# thislist[1:2] = ['blackcurrent','watermelon']
# print(thislist)

# thislst = ['apple','banana','cherry']
# thislst[1:3] = ['watermelon']
# print(thislst)


# thislist = ["apple","banana","cherry"]
# thislist.append("orange")
# print(thislist)


# thislist = ["apple","banana","cherry"]
# thislist.insert(1,"orange")
# print(thislist)

# thislist = ["apple","banana","cherry"]
# tropical = ["mango", "pineapple","papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.remove('banana')
# print(thislist)


# thislist = ["apple","banana","cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.clear()
# print(thislist)


