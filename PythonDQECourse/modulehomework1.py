#--------------------------create list of 100 random numbers from 0 to 100-----------------------
##---Using While for getting the 100 numbers from 0 to 100
# i = 0               # initiate the i with 0
# while i < 100:      # added the limit for i so that it would not exceed from 100
#     print(i)        # printing the 1
#     i = i +1        # getting the new value of i

#or we can use range as well
# for a in range(100):
#     print(a)


#--------------------------sort list from min to max (without using sort(),sorted())

# a = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]  # initiate the a with list of values
#
# for i in range(len(a)):                         #assigning the lenght of a to i
#     for j in range(i + 1, len(a)):              #assigning the lenght of a to J
#         if a[i] > a[j]:                         #if value of i (64) which is on place of 0 is greater than J (25) which is on place of 1
#            a[i], a[j] = a[j], a[i]              #then replace i with J else move forward and it will continue till range of i
#
# print(a)

#-------------------------Calculate average for even and odd numbers

