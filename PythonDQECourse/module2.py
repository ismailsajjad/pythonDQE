# #list
# a = ['a','b','d','f','g','e',True,123]   # this is list with squre braces
# print(a)
# print(type(a))  # check type of list

# #tuple
# b = ('a','b','d','f','g','e',True,123)   # this is tuble with Parentheses
# print(b)
# print(type(b))

##checking the index of a alphabat from string
# aa = 'IamfromPoland'
# print(aa)
# print(aa.index('P'))  #we can get the index of P
# print(aa[3])          #we can get the value of index 3 which is f. Index starts from 0
# print(aa[3:])  # It mean value of string will be starts from index 3. 3 will be included as well
# print(aa[3:-2])  # it means start from index 3 (from left to right) and ends on index -2 (from right to left) not incuded last 2 alphabat
# #We can also use indexing in tuple as well
# print(b[4])  # #printing the index4 value from tuple
# #append add elements into collection
# #if we want to add one more elements in tuple
# b.append('new')  ##while adding new elements in tuple we will receive 'tuple' object has no attribute 'append' because its immutable
# #we can use append in list like we have list a
# a.append('new')
# print(a)
# #len() to get the number of elements in collection
# ac = ('a','b','d','f','g','e',True,123)
# print("length", len(ac))
# ab = ('a','b','d','f','g','e',True,123)  #we can use for with tuple and list as well
# for i in ab:
#     print(i)
# #count() its use to get how many elements are in collection
# ae = ('a','b','d','f','gg','e')
# print(ae.count('gg'))
# #sort()
# #we can use sort in list and array not in tuple
# list_a = [1,2,3,5,8,9,4]
# print(list_a.sort()) # it will return NULL
# print(list_a)    # it will return  [1, 2, 3, 4, 5, 8, 9]
# print(sorted(list_a)) # it will return  [1, 2, 3, 4, 5, 8, 9]
# print(list_a)       # it will return  [1, 2, 3, 4, 5, 8, 9]
# #sorted()    sort will change the current list and sorted will

# #insert()  It allow us to add element in any position in list

# pop_list = [2,3,5,8,9,10]
# b = pop_list.pop(2)
# print(b)

# #pop it allow us to remove some elements
# The pop() function removes the last element or the element based on the index given. remove() function removes the first
# occurrence of the specified element.
#remove not working on tuple

# pop_list.remove(3)
# print(pop_list)

# #reverse it reverse the emlements from list not working on tuple
# reverse_list = [4,9,8,6,2,5,5]
# reverse_list.reverse()
# print(reverse_list)

#copy method
# #it will copy the list
# a_copy = [5,8,3,9,2]
# b_copy = a_copy.copy()
# a_copy.sort()
# print("a_copy" , a_copy)
# print("b_copy", b_copy)

# #Dictionary
# dic_a = {'a': 1,'d' : 43,(1,3,5) :88,True :99 }
# print(dic_a)
# print(type(dic_a))
# print(dic_a.get(True))
#
# # #update
# dic_a[(1,3,5)] = 99
# print(dic_a)

# #fromkeys
# b = dic_a.fromkeys([1,3,5],88)
# print(b)

# #keys(), values(), items()
# for key, value in dic_a.items():
#     print('this is key', key,  ' ; This is value', value)


# #creating dic

a_dic = {'name' : 'ismail', 'country':'PAK', 'year': '2023'}
print(a_dic)
print(a_dic['name'])
a_dic.setdefault('month','N/A')
print(a_dic['month'])

# #set
set_a = {1,3,5,8,8}
print(set_a)
set_a.add(9)
print(set_a)

