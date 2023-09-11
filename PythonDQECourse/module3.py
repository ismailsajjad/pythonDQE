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


