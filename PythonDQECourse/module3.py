# #String
# #sequence of character
# a = 'a'
a = '\u0063' # #this is unicode of c
print(a)

b = 'It\'s Monday'  # #backslash '\' is used for the addition of single comma
print(b)
ab = '\N{ROMAN NUMERAL EIGHT}'
print(ab)

# #Convert Method: capitalize(), lower(), upper(), swapcase, title()

aa = "I_am_in_poland@gmail.com"
print(aa.lower())        #string will change it to lower case
print(aa.upper())        #string will change it to upper case
print(aa.capitalize())   #first letter of string will be upper
print(aa.title())        #it give us each work stated from upper case
print(aa.swapcase())     #In the string lower will change in upper and vice virsa

# #check Methods
bb = "I_am_in_poland@gmail.com"
print(bb.startswith('I'))   #True Because it starts with 'I'
print(bb.islower())         #False Because upper alphabet is present
print(bb.isalnum())         #it checks if string is integer
print(bb.isalpha())         #it checks if string is only alphabet

# #Modify Method replace(), split(), splitlines(), join(), format()
# cc = "I am in poland com"
# cc.replace(' ', '/n')           #strings cannot be mutated or changed. We can assign strings to variables, and reassign new strings to the same variable, but individual characters within a string cannot be reassigned.
# print(cc)
# dd = cc.replace(' ', '\n')
# print(dd)
# ee = cc.replace('i', '**')  #replacing with symbol  answer: I am **n poland com
# print(ee)
# #split()
# ff = "i am in poland com"
# print(ff.split('i')) #it will replace i and split the string answer: ['', ' am ', 'n poland com']
# print(ff.split())   #it will split the string where space is mention  answer: ['i', 'am', 'in', 'poland', 'com']
# print(ff.split('i')[2]) #it means start from index 2 and replace i from that index and print rest of values result: n poland com

# #splitlines
ee = "i am in \npoland\n com"
print(ee.splitlines())    #results ['i am in ', 'poland', ' com']

# #join join different symbol in one string
gg = ['a','b','c']
gf = ''.join(gg)
print(gf)   #abc
import os
print(os.path.join("C:","User","IsmailSajjad"))


